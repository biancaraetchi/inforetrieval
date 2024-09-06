from django.urls import path

from . import views

urlpatterns = [
    path("", views.fetch_articles, name="index"),
    path("author_id/", views.fetch_author_id, name="author_id"),
]