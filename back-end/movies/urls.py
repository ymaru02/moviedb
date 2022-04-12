from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/actor/', views.actor_list),
    path('<int:movie_pk>/genre/', views.genre_list),
    path('<int:movie_pk>/movie/', views.movie_detail),
    path('<int:movie_pk>/review/', views.review_create),
    path('review/<int:review_pk>/', views.review_update_delete),
    
    # 장르 가져오기
    path('<int:genre_pk>/genre/movie/', views.genre_movie_list),
    path('genres/', views.genre_all_list),
    
    # 좋아요
    path('likes/', views.likes),
    path('<int:movie_pk>/likes/', views.movie_likes),

    # 추천
    path('<int:genre1_pk>/<int:genre2_pk>/recommend/', views.recommend_list),


    path('get_movie/', views.webCrollingMovie),
    path('get_actor/', views.webCrollingActor),
]