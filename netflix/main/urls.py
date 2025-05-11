from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('watch_movie/<int:movie_id>',views.watch_movie,name='watch_movie'),
]