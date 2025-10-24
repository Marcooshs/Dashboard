from django.test import SimpleTestCase


class SanityTest(SimpleTestCase):
    def test_math(self):
        self.assertEqual(1 + 1, 2)
