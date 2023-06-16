from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("detail/<slug:slugInput>/", views.details, name="detail"),
    path("kategori/<str:kategoriInput>/", views.kategori, name="kategori"),
    path("", views.index, name="index"),
]
