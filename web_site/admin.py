from django.contrib import admin

from .models import Actor, Category, Movie, Genre, Reviews, Rating, RatingStar, MovieShots


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('slug',)}

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('slug',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('slug',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Actor)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
