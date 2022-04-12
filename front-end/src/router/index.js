import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleList from '@/views/articles/ArticleList'
import ArticleForm from '@/views/articles/ArticleForm'
import ArticleDetail from '@/views/articles/ArticleDetail'
import UpdateArticle from '@/views/articles/UpdateArticle'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Home from '@/views/homes/Home'
import MovieDetailMain from '@/views/detail/MovieDetailMain'
import MovieDetailCrew from '@/views/detail/MovieDetailCrew'
import MovieDetailGrade from '@/views/detail/MovieDetailGrade'
import MovieDetailContents from '@/views/detail/MovieDetailContents'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
    // 개별 가드!
    // https://router.vuejs.org/kr/guide/advanced/navigation-guards.html#%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8B%E1%85%A7%E1%86%A8-%E1%84%80%E1%85%A1%E1%84%83%E1%85%B3
    beforeEnter: (to, from, next) => {
      next()
    }
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  // 자유게시판
  {
    path: '/articles',
    name: 'ArticleList',
    component: ArticleList,
  },
  {
    path: '/articles',
    name: 'ArticleDetail',
    component: ArticleDetail,
  },
  {
    path: '/articles/create',
    name: 'ArticleForm',
    component: ArticleForm,
  },
  {
    path: '/articles/update',
    name: 'UpdateArticle',
    component: UpdateArticle,
  },
  // 영화
  {
    path: '/movie/detail/main',
    name: 'MovieDetailMain',
    component: MovieDetailMain,
  },
  {
    path: '/movie/detail/crew',
    name: 'MovieDetailCrew',
    component: MovieDetailCrew,
  },
  {
    path: '/movie/detail/contents',
    name: 'MovieDetailContents',
    component: MovieDetailContents,
  },
  {
    path: '/movie/detail/grade',
    name: 'MovieDetailGrade',
    component: MovieDetailGrade,
  },  
]

const router = new VueRouter({
  mode: 'history',
  scrollBehavior(to) { 
    if (to.name === 'MovieDetailCrew' || to.name === 'MovieDetailContents'){
      return { x: 0, y: 600 } 
    }else if (to.name === 'MovieDetailMain'){
      return { x: 0, y: 0 }
    }
  },
  base: process.env.BASE_URL,
  routes
})

// 전역 가드
// https://router.vuejs.org/kr/guide/advanced/navigation-guards.html#%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8B%E1%85%A7%E1%86%A8-%E1%84%80%E1%85%A1%E1%84%83%E1%85%B3
router.beforeEach((to, from, next) => {
  const accessToken = localStorage.getItem('accessToken')
  if (to.name === 'Login' || to.name === 'Signup') {
    if (accessToken) {
      next({ name: 'Home' })
    }
  } else {
    if (!accessToken) {
      next({ name: 'Login' })
    }
  }
  next()
})


export default router
