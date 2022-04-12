from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND
)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    ArticleListSerializer, 
    ArticleSerializer,
    CommentSerializer
)
from .models import Article, Comment


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])    # 인증여부 설정
def article_list_create(request):
    '''
    GET : 자유게시판 리스트 가져오기
    POST : 자유게시글 등록하기
    '''
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        articles = Article.objects.order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    return Response({'message': '아직 지원하지 않는 기능입니다.'}, status=HTTP_404_NOT_FOUND)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def article_detail_update_delete(request, article_pk):
    '''
    GET : article_pk번 게시글 정보(JSON) 반환 
    PUT : article_pk번 게시글 수정
    DELETE : article_pk번 게시글 삭제
    '''
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if article.user == request.user :
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response({'message': '권한이 없는 사용자의 접근입니다.'}, status=HTTP_401_UNAUTHORIZED)
    elif request.method == 'DELETE':
        if article.user == request.user :
            article.delete()
            return Response({'message':f'{article_pk}번 게시글이 삭제되었습니다.'}, status=HTTP_204_NO_CONTENT)
        return Response({'message': '권한이 없는 사용자의 접근입니다.'}, status=HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    '''
    POST : article_pk번 게시글에 댓글 등록하기
    '''
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_pk):
    '''
    DELETE : comment_pk번 댓글 삭제
    '''
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'DELETE':
        if comment.user == request.user :
            comment.delete()
            return Response({'message': '해당 댓글이 삭제되었습니다.'}, status=HTTP_204_NO_CONTENT)
        return Response({'message': '권한이 없는 사용자의 접근입니다.'}, status=HTTP_401_UNAUTHORIZED)
