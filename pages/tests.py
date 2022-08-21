"""
David Barnes
CIS218
08-21-22
"""
from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    """Home Page Tests"""

    def test_url_exists_at_correct_location(self):
        """Test url exists at correct location"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """Test url available by name"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Test template name correct"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        """Test template content"""
        response = self.client.get(reverse("home"))
        self.assertContains(response, '<h1 class="display-5 fw-bold">David Barnes</h1>')


class ProjectsPageTests(SimpleTestCase):
    """Projects Page Tests"""

    def test_url_exists_at_correct_location(self):
        """Test url exists at correct location"""
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """Test url available by name"""
        response = self.client.get(reverse("projects"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Test template name correct"""
        response = self.client.get(reverse("projects"))
        self.assertTemplateUsed(response, "projects.html")

    def test_template_content(self):
        """Test template content"""
        response = self.client.get(reverse("projects"))
        self.assertContains(response, "<h1>Projects</h1>")


class ContactPageTests(SimpleTestCase):
    """Contact Page Tests"""

    def test_url_exists_at_correct_location(self):
        """Test url exists at correct location"""
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """Test url available by name"""
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Test template name correct"""
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")

    def test_template_content(self):
        """Test template content"""
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<h1>Contact</h1>")
