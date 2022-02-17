from django.urls import path
from .views import *

urlpatterns = [
    path('', MoviesView.as_view(), name='carousel_home'),
    path('<slug:slug>/', SingleMovieView.as_view(), name='movie_detail'),

]
