from .models import Article, Comment
from rest_framework import serializers


class CommentListSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article',)

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        # is_vailed에서 제외
        read_only_fields = ('article', 'user',) # model을 통해서 article을 불러올 수 있음


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = serializers.SerializerMethodField()
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.StringRelatedField(source='user.username', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_set', 'username', 'comment_count', 'user',)
        read_only_fields = ('user', 'like_users', )
    
    def get_comment_set(self, instance):
        comments = instance.comment_set.all().order_by('-id')
        return CommentListSerializer(comments, many=True).data


class ArticleListSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.StringRelatedField(source='user.username', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'created_at', 'user', 'username', 'comment_count', )
        read_only_fields = ('user', 'like_users',)