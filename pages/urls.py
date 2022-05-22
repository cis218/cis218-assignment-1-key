from django.urls import path
from .views import HomePageView, ProjectsPageView, ContactPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("projects/", ProjectsPageView.as_view(), name="projects"),
    path("contact/", ContactPageView.as_view(), name="contact"),
]
