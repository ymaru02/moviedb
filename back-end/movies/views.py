from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import os
from .serializers import (
    CrewListSerializer,
    MovieSerializer,
    MovieListSerializer,
    ActorListSerializer,
    CrewListSerializer,
    GenreListSerializer,
    Movie_Actor_RelationSerializer,
    Movie_Crew_RelationSerializer,
    Movie_Actor_RelationListSerializer,
    Movie_Crew_RelationListSerializer,
    ReviewListSerializer,
    ReviewSerializer,
)

from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_204_NO_CONTENT
)

from .models import (
    Actor,
    Crew,
    Genre,
    Movie, 
    Review,
    Movie_Actor_Relation,
    Movie_Crew_Relation,
)

# api으로 받아온 json파일 DB에 저장하기
import json
import urllib.request
from django.http import QueryDict
import requests
import pprint

@api_view(['GET'])
def movie_list(request):
    '''
    GET : 영화 조회하기
    '''
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    '''
    GET : 영화 상세조회하기
    '''
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def actor_list(request, movie_pk):
    '''
    GET : 출연진 조회하기
    '''
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        actors = movie.actors.all()
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def genre_list(request, movie_pk):
    '''
    GET : 장르 조회하기
    '''
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        genres = movie.genres.all()
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def genre_all_list(request):
    '''
    GET : 모든 장르 조회하기
    '''
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def genre_movie_list(request, genre_pk):
    '''
    GET : 해당 장르의 영화 조회하기
    '''
    if request.method == 'GET':
        genre = get_object_or_404(Genre, pk=genre_pk)
        movies = genre.movie_set.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
        

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def review_create(request, movie_pk):
    '''
    POST : movie_pk번 영화에 평점 등록하기
    '''
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT','DELETE'])
@permission_classes([IsAuthenticated]) 
def review_update_delete(request, review_pk):
    '''
    PUT : review_pk번 평점 수정
    DELETE : review_pk번 평점 삭제
    '''
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if review.user == request.user :
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response({'message': '권한이 없는 사용자의 접근입니다.'}, status=HTTP_401_UNAUTHORIZED)
    elif request.method == 'DELETE':
        if review.user == request.user :
            review.delete()
            return Response({'message': '해당 평점글이 삭제되었습니다.'}, status=HTTP_204_NO_CONTENT)
        return Response({'message': '권한이 없는 사용자의 접근입니다.'}, status=HTTP_401_UNAUTHORIZED)


# 좋아요
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_likes(request, movie_pk):
    '''
    POST: 좋아요/취소 반영하기
    '''
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'POST':
        # 좋아요 누른 상태 검사하기
        if movie.like_users.filter(pk=request.user.pk).exists():
            # 있으면 제거하기
            movie.like_users.remove(request.user)
        else:
            # 없으면 추가하기
            movie.like_users.add(request.user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

# 좋아요
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def likes(request):
    '''
    GET: 좋아요 확인
    '''
    if request.method == 'GET':
        movies = request.user.like_movies.all()

        result = {
            'id': [], 
            'title': [],
            'adult': [],
            'production_country':[],
            'vote_count': [],
            'vote_avg': [],
            'release_date': [],
            'genres':[],
        }
        for movie in movies:
            if movie.title: result['title'].append(movie.title)
            if movie.adult: result['adult'].append(movie.adult)
            if movie.production_country: result['production_country'].append(movie.production_country)
            if movie.vote_count: result['vote_count'].append(movie.vote_count)
            if movie.vote_avg: result['vote_avg'].append(movie.vote_avg)
            if movie.release_date: result['release_date'].append(movie.release_date)
            movie = get_object_or_404(Movie, pk=movie.pk)
            genres = movie.genres.all()
            for genre in genres: result['genres'].append(genre.id)

        # dict to QueryDict 변환
        query_dict = QueryDict('', mutable=True)    
        query_dict.update(result)
        return Response(query_dict)
        recommend_list

# 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_list(request, genre1_pk, genre2_pk):
    '''
    GET : 해당 장르의 영화 조회하기
    '''
    if request.method == 'GET':
        genre1 = get_object_or_404(Genre, pk=genre1_pk)
        genre2 = (get_object_or_404(Genre, pk=genre2_pk))
        movies = genre1.movie_set.all()
        movies.union(genre2.movie_set.all(), all=True)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
        

# Data 저장할 때 실행하시오.
def webCrollingMovie(request):
    ### api로 받아온 json 데이터 가공 과정
    params = {
          'api_key' : os.environ["TMDB_API_KEY"],
          'language' : 'ko-KR'
    }
    
    for j in range(1, 11):       # 1-10 page movie_id를 가져오기 위해서 실행
        url = 'https://api.themoviedb.org/3/movie/popular?api_key='+params['api_key']+'&page='+str(j)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf8'))
        get_data = data.get('results')
        for i in range(20):     # 20개 데이터
            id = get_data[i]['id']

            if Movie.objects.filter(pk=id).exists():    # movie_id가 존재하면 건너뜀
                continue
            else :      
                # movie_id가 존재하지 않으면 실행됨
                # movie_id에 매칭되는 영화 정보를 구하기 위해서 실행
                url1 = 'https://api.themoviedb.org/3/movie/'+str(id)+'?api_key='+params['api_key']+'&language='+params['language']
                response1 = urllib.request.urlopen(url1)  
                movie_data = json.loads(response1.read().decode('utf8'))

                # movie_id에 매칭되는 video key를 구하기 위해서 실행
                url2 = 'https://api.themoviedb.org/3/movie/'+str(id)+'/videos?api_key='+params['api_key']
                response2 = urllib.request.urlopen(url2)
                data2 = json.loads(response2.read().decode('utf8'))
                
                key = ''
                if data2.get('results'):
                    key = data2.get('results')[0]['key']

                production_country = ''
                if len(movie_data.get('production_countries')) :
                    production_country = movie_data.get('production_countries')[0]['name']
                
                back_path = ''
                if movie_data.get('backdrop_path'):
                    back_path = movie_data.get('backdrop_path')
                
                genres_len = len(movie_data.get('genres'))
                genres_ids = list()
                if genres_len :
                    for ids in range(genres_len):
                        genres_ids.append(movie_data.get('genres')[ids]['id'])
                
                result = {
                    'id': id,
                    'title': movie_data.get('title'),
                    'poster_path': movie_data.get('poster_path'),
                    'adult': movie_data.get('adult'),
                    'overview': movie_data.get('overview'),
                    'production_country': production_country,
                    'back_path': back_path,
                    'vote_count': movie_data.get('vote_count'),
                    'vote_avg': movie_data.get('vote_average'),
                    'video_key': key,
                    'runtime': movie_data.get('runtime'),
                    'release_date': movie_data.get('release_date'),
                }

                # dict to QueryDict 변환
                query_dict = QueryDict('', mutable=True)    
                query_dict.update(result)

                serializer = MovieSerializer(data=query_dict)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

                movies = Movie.objects.get(pk=id)
                for g in genres_ids:
                    # ManyToManyField인 중개테이블 genres 에 저장
                    movies.genres.add(g)

def webCrollingActor(request):
    ### api로 받아온 json 데이터 가공 과정
    params = {
          'api_key' : os.environ["TMDB_API_KEY"],
          'language' : 'ko-KR'
    }
    movies = Movie.objects.all()
    for movie in movies:
        # movie_id에 매칭되는 출연진 정보를 구하기 위해서 실행
        url = 'https://api.themoviedb.org/3//movie/'+str(movie.pk)+'/credits?api_key='+params['api_key']+'&language='+params['language']
        response = urllib.request.urlopen(url)  
        actor_data = json.loads(response.read().decode('utf8'))
        cast_len = len(actor_data.get('cast'))
        crew_len = len(actor_data.get('crew'))
    
        if cast_len:
            for i in range(cast_len):
                id = actor_data.get('cast')[i]['id']

                if Actor.objects.filter(pk=id).exists():
                    # pass
                    actor = get_object_or_404(Movie_Actor_Relation, actor=id)

                    actor_result = {
                        "known_for_department": actor_data.get('cast')[i]['known_for_department'],
                        "character": actor_data.get('cast')[i]['character'].replace('(uncredited)',''),
                        "order": actor.order,
                    }

                    if actor_result['known_for_department'] not in actor.known_for_department:
                        actor_result['known_for_department'] = actor.known_for_department + ',' + actor_result['known_for_department']
                    if actor_result['character'] not in actor.character:
                        actor_result['character'] = actor.character + ',' + actor_result['character']

                    query_dict = QueryDict('', mutable=True)    
                    query_dict.update(actor_result)

                    serializer = Movie_Actor_RelationSerializer(actor, data=query_dict)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                else :
                    path = ''
                    if actor_data.get('cast')[i]['profile_path']:
                        path = actor_data.get('cast')[i]['profile_path']

                    result = {
                        'id': id,
                        'type': 1,
                        'name': actor_data.get('cast')[i]['name'],
                        'profile_path': path,
                    }
                    actor_result = {
                        "known_for_department": actor_data.get('cast')[i]['known_for_department'],
                        "character": actor_data.get('cast')[i]['character'],
                        "order": actor_data.get('cast')[i]['order'],
                    }

                    # dict to QueryDict 변환
                    query_dict = QueryDict('', mutable=True)    
                    query_dict.update(result)

                    serializer = ActorListSerializer(data=query_dict)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                
                    # dict to QueryDict 변환
                    actor_query_dict = QueryDict('', mutable=True)    
                    actor_query_dict.update(actor_result)

                    actor = get_object_or_404(Actor, pk=id)
                    serializer = Movie_Actor_RelationSerializer(data=actor_query_dict)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save(movie=movie, actor=actor)

                # ManyToManyField인 중개테이블 actors 에 저장
                # movie.actors.add(id)

        if crew_len:
            for j in range(crew_len):
                id = actor_data.get('crew')[j]['id']

                if Crew.objects.filter(pk=id).exists():
                    crew = get_object_or_404(Movie_Crew_Relation, crew=id)

                    crew_result = {
                        "known_for_department": actor_data.get('crew')[j]['known_for_department'],
                        "department": actor_data.get('crew')[j]['department'],
                        "job": actor_data.get('crew')[j]['job']
                    }

                    if crew_result['known_for_department'] not in crew.known_for_department:
                        crew_result['known_for_department'] = crew.known_for_department + ',' + crew_result['known_for_department']
                    if crew_result['department'] not in crew.department:
                        crew_result['department'] = crew.department + ',' + crew_result['department']
                    if crew_result['job'] not in crew.job:
                        crew_result['job'] = crew.job + ',' + crew_result['job']

                    query_dict = QueryDict('', mutable=True)    
                    query_dict.update(crew_result)

                    serializer = Movie_Crew_RelationSerializer(crew, data=query_dict)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                else :
                    path = ''
                    if actor_data.get('crew')[j]['profile_path']:
                        path = actor_data.get('crew')[j]['profile_path']

                    result = {
                        'id': id,
                        'type': 2,
                        'name': actor_data.get('crew')[j]['name'],
                        'profile_path': path,
                    }

                    crew_result = {
                        "known_for_department": actor_data.get('crew')[j]['known_for_department'],
                        "department": actor_data.get('crew')[j]['department'],
                        "job": actor_data.get('crew')[j]['job']
                    }

                    # dict to QueryDict 변환
                    query_dict = QueryDict('', mutable=True)    
                    query_dict.update(result)

                    serializer = CrewListSerializer(data=query_dict)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()

                    # dict to QueryDict 변환
                    crew_query_dict = QueryDict('', mutable=True)    
                    crew_query_dict.update(crew_result)

                    crew = get_object_or_404(Crew, pk=id)
                    serializer = Movie_Crew_RelationSerializer(data=crew_query_dict)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save(movie=movie, crew=crew)
