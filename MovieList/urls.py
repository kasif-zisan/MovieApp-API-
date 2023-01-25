from django.urls import path
from MovieList import views
urlpatterns = [
    path('movies/', views.showMovie),
    path('movies/<int:pk>/', views.MovieDetails)
]
