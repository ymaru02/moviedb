# README

[TOC]

## i. 팀원 정보 및 업무 분담 내역 

	### 	팀원 정보

​		팀장: 🐰`대전_1반_이소라`

​		팀원: 🐰`대전_1반_윤동희`



### 기간

- *2021.10.17* : 명세서 기반으로 디자인 및 컨셉 설정, 영화 데이터  API 결정, ERD, 업무 분담
- *2021.10.18~10.19* : 구현 기능 정리, Home 틀 제작, Detail 틀 제작, 로고 제작, 영화 데이터 update 및 actor/ genre api 구현
- *2021.10.20~10.21* :  (Home, Detail) UI 마크업 및 스타일링, 데이터 추가, 로그인 페이지, key정보를 통한 iframe 영상 구현
- *2021.10.21~10.22* :  평점 시스템, 자유 게시판,  (Login) UI 마크업 및 스타일링
- *2021.10.23~10.24* :  추천 알고리즘,  검색바, viewport에 맞게 영상 (자유 게시판 평점, 시스템) UI 마크업 및 스타일링
- *2021.10.25* : 코드 리뷰 및 리펙토링, 발표 준비하기 (PPT 및 대본 준비)
- *2021.10.26* : 발표



### 	업무 분담 내역

Client - 윤동희

Server - 이소라



## ii. 목표 서비스 구현 및 실제 구현 정도 

### 목표 서비스 구현

- 로그인, 로그아웃
- 홈, 알고리즘 추천 시스템 
- 디테일 페이지
- 자유 게시판, 평점 시스템, 댓글, 리뷰
- 검색
- 프로필 페이지



### 실제 구현 정도

- 로그인, 로그아웃
- 홈, 알고리즘 추천 시스템 
- 디테일 페이지
- 자유 게시판, 평점 시스템, 댓글, 리뷰
- 검색



## iii. 데이터베이스 모델링 (ERD) 

#### 첫 구상 ERD

![Final-PJT](README.assets/Final-PJT.png)

#### 마지막 ERD

![Final-PJT (1)](README.assets/Final-PJT (1).png)

## iv. 필수 기능에 대한 설명 

### 필수 기능

#### 	A. 관리자 뷰

> 관리자 권한의 유저만 영화 등록/수정/삭제 권한을 가집니다.
> 관리자 권한의 유저만 유저 관리 권한을 가집니다. 
> 장고에서 기본적으로 제공하는 admin 기능을 이용하여 구현합니다. 
> Django admin기능을 이용하여 구현할 수 있습니다.



#### 	B. 영화 정보

>TMDB API를 이용한 DataBase
>
>영화 

![image-20211126013306991](README.assets/image-20211126013306991.png)

```python
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
```

```python
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
```

```python 
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

```



> Detail 페이지
>
> 주요 정보

![image-20211126013833473](README.assets/image-20211126013833473.png)



>출연제작

![image-20211126014046634](README.assets/image-20211126014046634.png)



> 영상 포토

![image-20211126014022561](README.assets/image-20211126014022561.png)



> 평점

![image-20211126014135169](README.assets/image-20211126014135169.png)



#### C. 검색

![image-20211126014226004](README.assets/image-20211126014226004.png)



![image-20211126013403707](README.assets/image-20211126013403707.png)



#### 	D. 영화 추천 알고리즘

> 관심 데이터 등록
>
> 유저의 정보를 통한 관심 영화 데이터 획득
>
> 영화 장르에 대한 정보 요청

![image-20211126014306688](README.assets/image-20211126014306688.png)



> 좋아요 등록
>
> 알고리즘 추천

![image-20211126014355076](README.assets/image-20211126014355076.png)

```vue
	loadLikeMovies: function({ commit, state }) {
      axios.get(`http://127.0.0.1:8000/movies/likes/`, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
      .then((res) => {
        commit('LOAD_LIKE_MOVIES', res.data)
      })    

    // 좋아요
    LOAD_LIKE_MOVIES: function(state, results) {
      state.movieLikes = results
    },

	axios.get(`http://127.0.0.1:8000/movies/${ this.genres[0] }/${ this.genres[1] }/recommend/`, {
      headers: {
        Authorization: `Bearer ${this.$store.state.accessToken}`
      }
    })
      .then((res) => {
       for (let index = 0; index < res.data.length / 5; index++) {
          this.movieCardsArray.push(res.data.slice(index * 5, (index + 1) * 5))
        }
      })
```



> 2가지 장르의 영화 데이터 조합하여 영화 데이터 획득

```python
    if request.method == 'GET':
        genre1 = get_object_or_404(Genre, pk=genre1_pk)
        genre2 = (get_object_or_404(Genre, pk=genre2_pk))
        movies = genre1.movie_set.all()
        movies.union(genre2.movie_set.all(), all=True)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
```



>추천 영화 데이터

```vue
        <div
          v-for="(movieCardList, index) in this.movieCardsArray"
          :key="index"  
          class="carousel-item" data-bs-interval="20000"
          :class="{ active: movieCardsArray[0] == movieCardList }"
        >
          <div class="row row-cols-md-3 row-cols-lg-5 g-4">
            <MovieGenreCard
              v-for="movieCard in movieCardList"
              :key="movieCard.id"
              :MovieGenreCard="movieCard"
            />
```



#### 	E. 커뮤니티

> 게시글, 댓글 모델

![image-20211126014559222](README.assets/image-20211126014559222.png)

![image-20211126014536924](README.assets/image-20211126014536924.png)

```python 
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 좋아요
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```



>게시글 
>
>GET POST PUT DELETE 이용

```python
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

```



> Client 와  Sever의 데이터 통신

```vue
loadArticleDetail: function ({ state, commit }, articleId) {
      axios.get(`http://127.0.0.1:8000/community/${articleId}/`, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then((res) => {
          commit('LOAD_ARTICLE_DETAIL', res.data)
        })
    },
    deleteArticle ({ commit, state }, article) {
      axios.delete(`http://127.0.0.1:8000/community/${article.id}/`, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then((res) => {
          if (res.status == 204) {
            commit('DELETE_ARTICLE', article) 
            router.push({ name: 'ArticleList' })
          }
        })
        .catch((error)=>{
          alert(error.response.data['message'])
        })
    },
    updateArticle ({ commit, state }, targetArticle) {
      axios.put(`http://127.0.0.1:8000/community/${targetArticle.id}/`, targetArticle, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then(res => {
          commit('UPDATE_ARTICLE', res.data)
          router.push({ name: 'ArticleDetail', query: { articleId: targetArticle.id }})
        })
        .catch((error)=>{
          alert(error.response.data['message'])
        })
    },
    createArticle ({ commit, state}, newArticle) {
      axios.post('http://localhost:8000/community/', { ...newArticle }, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then(response => {
          commit('SET_ARTICLES', response.data)
          router.push({ name: 'ArticleList' })
        })
        .catch(error => {
          alert(error.response.data['title'])
          alert(error.response.data['content'])
        })
    },
```





#### 	F. 댓글

>댓글
>
>GET POST PUT DELETE 이용
>
>Client 와 Sever 데이터 통신


![image-20211126014623339](README.assets/image-20211126014623339.png)

```python

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

```



#### G. 로그인 회원가입

> 로그인

![image-20211126012902046](README.assets/image-20211126012902046.png)



> 회원가입

![image-20211126012920718](README.assets/image-20211126012920718.png)

#### H. 평가

> 평가하기

![image-20211126014806295](README.assets/image-20211126014806295.png)



## v. 배포 서버 URL 

(배포를 아직 하지 못해서 배포서버 URL이 존재하지 않음)





## vi. 기타 (느낀 점)

#### 이소라

배우면서 알게 된 지식들도 많았지만,  DJango, Vue, JavaSpring, Python을 통해 프로젝트를 진행하면서 실전에서 배우는 게 더 많은 하루하루였습니다.

프로젝트에 적용한다고 생각하니 그동안 배웠던 내용들이 헷갈리기도 하고, 이해를 잘못했던 부분도 있었는데 프로젝트를 해내야한다는 사명감에 그러한 부분들을 찾아가는 과정을 통해서 많이 배웠습니다.

처음에 팀장으로서 동희님께 프로젝트의 루틴대로 설계와 구현을 주장하였는데, 논리적으로 제대로 설득하지 못해서 의견충돌이 났었습니다. 이 경험을 통해서 제가 알고 있는 기술 및 개발 지식이 많이 부족하다는 걸 느꼈고 협업하는데 있어서는 옳은 방향이어도 상대방을 설득할 수 없을 때 의견충돌이 발생한다는 점을 깨달았습니다. 개발자로 다른 개발자 및 클라이언트와 소통하기 위해서는 명확한 지식으로 상대방을 설득할 수 있는 지식이 저에게 있어야 협업을 더 잘할 수 있겠다는 사실을 느껴 방학중에 CS 공부를 더욱 열심히 해야겠다는 동기부여가 되는 일주일이었습니다.

그동안 실무에서 프론트와 백을 구분하지 않고 사용했었는데 이번 프로젝트로 프론트와 백을 나눠서 개발을 진행하며 백이 하는 일에 대해 좀 더 알 수 있었습니다. 백에서 api를 구성해 구현된 데이터를 가지고 프론트에서 해당 데이터를 통해 화면을 구성하고 프론트에서도 데이터를 커스텀해서 알고리즘을 구현하는 과정을 보며 개발자로서 더 배우고 싶다는 생각이 들었습니다.

초반에 충돌로 인해 둘다 서로를 이해하기 위해 백/프론트를 번갈아가면서 진행해서 각자 해당 포지션을 이해하는데 시간이 많이 소요되었지만, 전체적인 프로젝트의 흐름을 이해하고 공부하기에는 좋은 방법이었습니다.







#### 윤동희

일주일간 정말 많은 학습을 하게 되었다. DJango, Vue, JavaSpring, Python를 정말 많이 배우는 계기 였다.  그전까지 열심히 공부했다고 생각했었는데.... 정말로 프로젝트를 시작하니 어떻게 사용해 하는지 잘 이해가 안되었고 정말 많은 학습을 하였다.

하나하나 만들어 나아가며 신기하고 재미는 더욱 느끼게 되었고 프론트와 백이 왜 나누어진건지 알게 되었다.

중간중간 필요한 데이터를 위해 서버를 직접 구현하였고 어떻게 데이터를 가지고 와서 어떻게 사용하는지에 대해 많은 이해를 할 수 있었다.

프로젝트를 통해 서로 이해 못하는 부분에 대해 질문을 하며 자신의 의견에 대해 말하였고 중간 중간 의견 충돌이 있을 경우에는 상대방에 말을 들어보고 자신의 말을 하며 조율하였다. 

서버와 클라이언트를 둘 다 하며 협업을 처음 잘 나누어야 한다고 느끼게  되었지만 서버와 클라이언트 둘 다 학습 하여 많은 이해를 할 수 있었다.





