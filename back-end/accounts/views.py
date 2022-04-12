from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    '''
    POST : 회원가입 기능
    '''
    # 비밀번호 일치 확인 작업!
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')
    if password != password_confirmation:
        return Response({
            'password': ['비밀번호가 일치하지 않습니다']
        }, HTTP_400_BAD_REQUEST)
        
    # serializer 인스턴스 준비!
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # 유효성 검사 통과!
        user = serializer.save()
        # DB 열어보니까 저장은 잘 됨
        # hash password
        user.set_password(password)
        user.save()

        return Response(serializer.data, HTTP_201_CREATED)
    
