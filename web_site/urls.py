from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60 * 10)(MoviesView.as_view()), name='home'),
    path('catalog/<int:page>/', cache_page(60 * 10)(CatalogView.as_view()), name='catalog'),
    path('filter/', cache_page(60 * 10)(FilterMoviesView.as_view()), name='filter'),
    path('search/', cache_page(60 * 10)(Search.as_view()), name='search'),
    path('about/', cache_page(60 * 10)(about_us), name='about'),
    path('help/', cache_page(60 * 10)(faq_page), name='help_page'),
    path('register/', cache_page(60 * 10)(UserRegisterView.as_view()), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('catalog/<slug:slug>/<int:page>/', cache_page(60 * 10)(CatalogView.as_view()), name='genre_catalog'),
    path('<slug:slug>/', cache_page(60 * 5)(SingleMovieView.as_view()), name='movie_detail'),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/<int:page>/", cache_page(60 * 10)(ActorDetailView.as_view()), name="actor_detail"),
    path("producer/<str:slug>/<int:page>/", cache_page(60 * 10)(DirectorDetailView.as_view()), name="director_detail"),
]
