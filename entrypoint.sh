#!/usr/bin/env sh
set -e

echo "Aguardando o banco de dados em ${DB_HOST}:${DB_PORT:-5432}..."
# Tenta conectar até conseguir
RETRIES=30
i=0
while ! python - <<'PY'
import os, sys
import psycopg
try:
    psycopg.connect(
        host=os.environ.get('DB_HOST', '127.0.0.1'),
        port=os.environ.get('DB_PORT', '5432'),
        dbname=os.environ.get('DB_NAME', ''),
        user=os.environ.get('DB_USER', ''),
        password=os.environ.get('DB_PASSWORD', '')
    ).close()
    sys.exit(0)
except Exception as e:
    sys.exit(1)
PY
do
  i=$((i+1))
  if [ "$i" -ge "$RETRIES" ]; then
    echo "Erro: não consegui conectar ao Postgres após ${RETRIES} tentativas."
    exit 1
  fi
  echo "Banco ainda indisponível... tentando de novo ($i/$RETRIES)"
  sleep 2
done
echo "Banco disponível! ✅"

echo "Aplicando migrações..."
python manage.py migrate --noinput

echo "Coletando estáticos (se configurado)..."
python manage.py collectstatic --noinput || true

if [ "$DEBUG" = "True" ] || [ "$DEBUG" = "1" ]; then
  echo "Iniciando servidor de desenvolvimento..."
  exec python manage.py runserver 0.0.0.0:8000
else
  echo "Iniciando Gunicorn (produção)..."
  exec gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 60
fi
