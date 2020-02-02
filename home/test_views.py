from django.test import TestCase

class TestHomeViews(TestCase):
    
    def test_get_index_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')