from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Actor(models.Model):
    id = models.IntegerField(primary_key=True)          # 출연진 pk
    type = models.IntegerField()                        # 1: cast 2: Director
    name = models.CharField(max_length=500)             # 이름
    profile_path = models.TextField(blank=True)         # 프로필
    
    def __str__(self):
        return self.name


class Crew(models.Model):
    id = models.IntegerField(primary_key=True)          # 출연진 pk
    type = models.IntegerField()                        # 1: cast 2: Director
    name = models.CharField(max_length=500)             # 이름
    profile_path = models.TextField(blank=True)         # 프로필

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)          # 영화pk
    title = models.CharField(max_length=200)            # 영화제목
    poster_path = models.TextField(blank=True)          # 영화 포스터path
    adult = models.BooleanField(default=False)          # 성인여부
    overview = models.TextField(blank=True)             # 개요(줄거리)
    production_country = models.TextField(blank=True)   # 생산국가
    back_path = models.TextField(blank=True)            # 배경 path
    vote_count = models.IntegerField()                  # 평점 수
    vote_avg = models.FloatField(default=0)             # 평점 평균
    video_key = models.TextField(blank=True)            # 영화 예고편 key
    runtime = models.IntegerField()                     # 상영시간
    release_date = models.TextField()                   # 출시일
    genres = models.ManyToManyField(Genre)              # 장르

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')   # 좋아요
    
    def __str__ (self):
        return self.title


class Movie_Actor_Relation(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_actors', on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, related_name='actor_movies', on_delete=models.CASCADE)
    known_for_department = models.TextField(blank=True) 
    character = models.TextField(blank=True)
    order = models.IntegerField()

    def __str__ (self):
        return f'{self.actor}'


class Movie_Crew_Relation(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_crews', on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, related_name='crew_movies', on_delete=models.CASCADE)
    known_for_department = models.TextField(blank=True)  
    job = models.TextField(blank=True)  
    department = models.TextField(blank=True)  
    
    def __str__ (self):
        return f'{self.crew}'


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grade = models.IntegerField()
    content = models.CharField(max_length=300)
    
    def  __str__(self):
        return f'{self.id}'
