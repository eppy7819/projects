from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.first_page, name="first_page"),
    path('movie_list/', views.movie_list, name="movie_list"),
    path('recent_movie/', views.recent_movie, name="recent_movie"),
    path('<int:movie_pk>/', views.movie_detail, name="movie_detail"),
    path('<int:movie_pk>/update', views.movie_update, name="movie_update"),
    path('<int:movie_pk>/delete', views.movie_delete, name="movie_delete"),
    path('review_list/', views.review_list, name="review_list"),
    path('<int:movie_pk>/review_create/', views.review_create, name='review_create'),
    path('<int:movie_pk>/<int:review_pk>', views.review_detail, name='review_detail'),
    path('<int:movie_pk>/<int:review_pk>/review_update/', views.review_update, name='review_update'),
    path('<int:movie_pk>/<int:review_pk>/review_delete/', views.review_delete, name='review_delete'),
    path('<int:movie_pk>/<int:review_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:movie_pk>/<int:review_pk>/<int:comment_pk>/comment_delete/', views.comment_delete, name='comment_delete'),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('emotion/<int:pk>', views.emotion, name="emotion"),
    path('emotion_remove/', views.emotion_remove, name="emotion_remove"),
    path('search/search_result', views.search_result, name="search_result"),
]