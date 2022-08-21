"""
David Barnes
CIS218
08-21-22
"""
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Show Home Page"""

    template_name = "home.html"


class ProjectsPageView(TemplateView):
    """Show Projects Page"""

    template_name = "projects.html"


class ContactPageView(TemplateView):
    """Show Contact Page"""

    template_name = "contact.html"
