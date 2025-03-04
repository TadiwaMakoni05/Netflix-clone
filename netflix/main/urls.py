from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('watch_movie/<int:movie_id>',views.watch_movie,name='watch_movie'),
]