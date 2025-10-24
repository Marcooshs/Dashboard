// Tooltips Bootstrap
document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => new bootstrap.Tooltip(el));

// Tema claro/escuro usando localStorage
(function () {
  const html = document.documentElement;
  // aplica preferência salva
  const stored = localStorage.getItem('bs-theme');
  if (stored) html.setAttribute('data-bs-theme', stored);

  // alterna no clique
  const btn = document.getElementById('themeToggle');
  if (btn) {
    btn.addEventListener('click', () => {
      const next = html.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-bs-theme', next);
      localStorage.setItem('bs-theme', next);
    });
  }
})();
