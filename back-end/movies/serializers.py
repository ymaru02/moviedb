from django.db.models import fields
from rest_framework import serializers
from .models import (
    Actor,
    Genre,
    Movie,
    Crew,
    Movie_Actor_Relation,
    Movie_Crew_Relation,
    Review,
)

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class CrewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = '__all__'


        
class Movie_Actor_RelationSerializer(serializers.ModelSerializer):
    actor = ActorListSerializer(read_only=True)

    class Meta:
        model = Movie_Actor_Relation
        fields = '__all__'
        # is valid 에서 제외
        read_only_fields = ('movie', 'actor',)

class Movie_Crew_RelationSerializer(serializers.ModelSerializer):
    crew = CrewListSerializer(read_only=True)
    
    class Meta:
        model = Movie_Crew_Relation
        fields = '__all__'
        # is valid 에서 제외
        read_only_fields = ('movie', 'crew',)

class Movie_Actor_RelationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie_Actor_Relation
        fields = '__all__'

class Movie_Crew_RelationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_Crew_Relation
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        # is valid 에서 제외
        read_only_fields = ('user', 'movie',)


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        # is valid 에서 제외
        read_only_fields = ('user', 'movie', 'username',)


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreListSerializer(many=True, read_only=True)
    movie_actors = Movie_Actor_RelationSerializer(many=True, read_only=True)
    movie_crews = Movie_Crew_RelationSerializer(many=True, read_only=True)
    movie_reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'adult', 'production_country',
         'back_path', 'vote_count', 'vote_avg', 'overview', 'video_key', 'runtime', 'release_date',
          'genres', 'movie_actors', 'movie_crews', 'movie_reviews', 'like_users')
        read_only_fields = ('movie_actors','genres','movie_crews', 'movie_reviews', 'like_users')

class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    # movie_actors = serializers.StringRelatedField(many=True)
    # movie_crews = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'adult', 'production_country',
         'back_path', 'vote_count', 'vote_avg', 'video_key', 'runtime', 'release_date',
          'genres', )
