from django.urls import path, include
from books import views

urlpatterns = [
    path("api/", include('books.api.urls')),
    path('create_user/', views.create_user)
]
