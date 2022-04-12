import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import _ from 'lodash'

Vue.use(Vuex)

// axios.defaults.baseURL = ''

export default new Vuex.Store({
  state: {
    accessToken: '',
    // 자유게시판
    articles: [],
    article: [],
    comment: [],

    // 영화
    movieCards: [], 
    movieCard: [],
    movieCardArray: [],
    movieList: [],
    review: [],

    // 장르
    genreCards: [],
    genreMovieCards: [],

    // 좋아요 확인
    movieLike: false,
    movieLikes: [],

    // 감독
    producerCard: [],
  },
  getters: {
    isLogin: (state) => {
      return !!state.accessToken
    },
    getUsername: (state) => {
      return JSON.parse(atob(state.accessToken.split('.')[1])).username
    },
    getGenrePick: (state) => {
      return _.sampleSize(state.genreCards, 7)
    },
    getWriteReview: (state) => {
      let find = false
      if (state.movieCard.movie_reviews != undefined) {
        for (let index = 0; index < state.movieCard.movie_reviews.length; index++) {
          if (JSON.parse(atob(state.accessToken.split('.')[1])).username === state.movieCard.movie_reviews[index].username) {
            find = true
          }
        }
      }
      return find
    },
    getRecommend: (state) => {
      return _.sampleSize(state.movieLikes.genres, 2)
    } 
  },
  mutations: {
    setToken (state, newAccessToken) {
      state.accessToken = newAccessToken
    },
    deleteToken (state) {
      state.accessToken = ''
    },
    
    // 자유게시판 데이터
    SET_ARTICLES (state, newArticle) {
      state.articles = newArticle
    },
    DELETE_ARTICLE (state, targetArticle) {
      state.articles.splice(state.articles.indexOf(targetArticle.id), 1)
    },
    UPDATE_ARTICLE (state, targetArticle) {
      state.articles = state.articles.map(article => {
        if (article.id === targetArticle.id) {
          return targetArticle
        } else {
          return article
        }
      })
    },
    LOAD_ARTICLE_DETAIL: function (state, results) {
      state.article = results
    },
    CREATE_COMMENT: function (state, newComment) {
      state.comment = newComment
    },
    DELETE_COMMENT (state, targetCommentId){
      state.article.comment_set.splice(state.article.comment_set.indexOf(targetCommentId), 1)
    },

    // 영화 데이터 생성
    CREATE_MOVIE: function (state, movieItem) {
      state.movieList.push(movieItem)
    },
    // 영화 카드 모두 가져오기
    LOAD_MOVIE_CARDS: function (state, results) {
      // 전체 데이터
      state.movieCards = results
      
      // 카드 5개씩 구분
      for (let index = 0; index < results.length / 5; index++) {
        state.movieCardArray.push(results.slice(index * 5, (index + 1) * 5))
      }
    },
    // 해당 영화 카드 가져오기
    LOAD_MOVIE_CARD: function (state, results) {
      // 전체 데이터
      state.movieCard = results
    },
    
    // 영화 데이터
    SET_MOVIES: function (state, movies) {
      state.movieList = movies
    },
    // 영화 평점 데이터
    ADD_REVIEW: function (state, newReview) {
      state.review = newReview
    },

    DELETE_REVIEW (state, targetReviewId) {
      state.movieCard.movie_reviews.splice(state.movieCard.movie_reviews.indexOf(targetReviewId), 1)
    },
    UPDATE_REVIEW (state, targetReview) {
      state.movieCard.movie_reviews = state.movieCard.movie_reviews.map(review => {
        if (review.id === targetReview.id) {
          return targetReview
        } else {
          return review
        }
      })
    },

    // 모든 장르
    LOAD_GENRE_CARDS: function (state, results) {
      state.genreCards = results
    },
    LOAD_GENRE_MOVIE_CARDS: function (state, results) {
      state.genreMovieCards = results
    },

    // 좋아요
    LOAD_LIKE_MOVIES: function(state, results) {
      state.movieLikes = results
    },
    LIKE_MOVIE: function(state, results) {
      state.movieLike = results.like_users.some( user_id => {
        return user_id === JSON.parse(atob(state.accessToken.split('.')[1])).user_id
      }) 
    },
  },
  actions: {
    getToken ({ commit }, { username, password }) {
      axios.post('http://localhost:8000/api/token/', { username, password })
        .then(response => {
          localStorage.setItem('accessToken', response.data.access)
          commit('setToken', response.data.access)
          router.push({ name: 'Home' })
        })
    },
    // 자유게시판
    getArticles ({ commit, state }) {
      axios.get('http://127.0.0.1:8000/community/', {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then(response => {
          commit('SET_ARTICLES', response.data)
        })
    },
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
    createComment ({ commit, dispatch, state  }, { newComment, articleId } ) {
      axios.post(`http://localhost:8000/community/${articleId}/comments/`, { ...newComment }, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then(res => {
          commit('CREATE_COMMENT', res.data)
          dispatch('loadArticleDetail', articleId)
        })
        .catch(err => {
          alert(err.response.data['content'])
        })
    },
    deleteComment({ commit, dispatch, state}, { commentId, articleId}) {
      axios.delete(`http://localhost:8000/community/comments/${commentId}/`, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then((res) => {
          if (res.status == 204) {
            commit('DELETE_COMMENT', commentId)
            dispatch('loadArticleDetail', articleId)
          }
        })
        .catch((error)=>{
          alert(error.response.data['message'])
        })
    },
    loadMovieCards: function ({ commit }) {
      axios.get('http://127.0.0.1:8000/movies/')
        .then((res) => {
          commit('LOAD_MOVIE_CARDS', res.data)
          // console.log(res.data)
        })
    },
    loadMovieCard: function ({ commit }, movieId) {
      axios.get(`http://127.0.0.1:8000/movies/${movieId}/movie/`)
        .then((res) => {
          commit('LOAD_MOVIE_CARD', res.data)
        })
    },
    readMovie: function({ commit }) {
      const movies = JSON.parse(localStorage.getItem('movieList')) || []
      commit('SET_MOVIES', movies)
    },
    createReview ({ commit, dispatch, state }, { newReview, movieId } ) {
      axios.post(`http://localhost:8000/movies/${movieId}/review/`, { ...newReview }, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        } 
      })
        .then(response => {
          commit('ADD_REVIEW', response.data)
          dispatch('loadMovieCard', movieId)
        })
        .catch(error => {
          // console.log(error)
          alert(error.response.data['content'])
        })
    },
    deleteReview ({ commit, dispatch, state }, {reviewId, movieId}) {
      axios.delete(`http://127.0.0.1:8000/movies/review/${reviewId}/`, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then((res) => {
          if (res.status == 204) {
            commit('DELETE_REVIEW', reviewId)
            dispatch('loadMovieCard', movieId)
          }
        })
        .catch((error)=>{
          alert(error.response.data['message'])
        })
    },
    addReview ({ commit, state }, reviewId) {
      axios.get(`http://127.0.0.1:8000/movies/review/${reviewId}/`, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then((res) => {
          commit('ADD_REVIEW', res.data)
        })
        .catch((error)=>{
          alert(error.response.data['message'])
        })
    },
    updateReview ({ commit, dispatch, state }, {targetReview, movieId }) {
      axios.put(`http://127.0.0.1:8000/movies/review/${targetReview.id}/`, targetReview, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then(res => {
          commit('UPDATE_REVIEW', res.data)
          dispatch('loadMovieCard', movieId)
        })
        .catch((error)=>{
          alert(error.response.data['message'])
        })
    },
    loadGenres: function({ commit }) {
      axios.get(`http://127.0.0.1:8000/movies/genres/`)
        .then((res) => {
          commit('LOAD_GENRE_CARDS', res.data)
        })
    },
    loadGenreMovies: function({ commit }, genreId) {
      axios.get(`http://127.0.0.1:8000/movies/${genreId}/genre/movie/`)
      .then((res) => {
        commit('LOAD_GENRE_MOVIE_CARDS', res.data)
      })
    },

    // 좋아요
    loadLikeMovie: function({ commit, state }, movieId) {
      axios.get(`http://127.0.0.1:8000/movies/${movieId}/likes/`, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
      .then((res) => {
        commit('LIKE_MOVIE', res.data)
      })
    },
    updateLikeMovie: function({ commit, state }, movieId) {
      axios.post(`http://127.0.0.1:8000/movies/${movieId}/likes/`, { }, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        } 
      })
      .then((res) => {
        commit('LIKE_MOVIE', res.data)
      })
    },
    // 좋아요 영화들
    loadLikeMovies: function({ commit, state }) {
      axios.get(`http://127.0.0.1:8000/movies/likes/`, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
      .then((res) => {
        commit('LOAD_LIKE_MOVIES', res.data)
      })
    },
    // 추천 영화
    loadRecommedMovies: function({ commit, state}, genres) {
      console.log(genres)
      axios.get(`http://127.0.0.1:8000/movies/${genres[0].id}/${genres[1].id}/recommend/`, {
        headers: {
          Authorization: `Bearer ${state.accessToken}`
        }
      })
      .then((res) => {
        commit('LOAD_LIKE_MOVIES', res.data)
      })
    }
  }
})
