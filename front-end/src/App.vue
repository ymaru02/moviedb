<template>
  <div id="app" class="back-ground">
    <nav class="navbar navbar-expand-lg navbar-light back_ground" id="nav">
      <div class="container-fluid" >
        <div class="col-2">
          <router-link class="navbar-brand" to="/">
            <img src="@/assets/logo2.png" alt="" class="d-inline-block align-text-top w-50 img_back_ground">
          </router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
        <div class="col">
          <div class="collapse navbar-collapse " id="navbarSupportedContent">
            <ul class="navbar-nav m-auto mb-2 mb-lg-0 menu ">
              <li class="nav-item ">
                <router-link class="nav-link active" aria-current="page" :to="{ name: 'Home' }" >Movie </router-link>
              </li>
              <li class="nav-item ">
                <router-link class="nav-link active" aria-current="page" to=""> | </router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link active" aria-current="page" :to="{ name: 'ArticleList' }">Free board </router-link>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-2">
          <div class="collapse navbar-collapse d-flex justify-content-end" id="navbarSupportedContent">
            <div v-if="isLogin" class="list-inline login_active login_font">
              <li class="nav-item list-inline-item login_user_active">{{ getUsername }} </li>
              <li class="nav-item list-inline-item " @click="logout"> Logout </li>
            </div>
            <div v-else class="list-inline">
              <li class="nav-item list-inline-item">
                <router-link class="nav-link active" aria-current="page" :to="{ name: 'Signup' }">Signup</router-link>
              </li>
              <li class="nav-item list-inline-item">
                <router-link class="nav-link active" aria-current="page" :to="{ name: 'Login' }">Login</router-link> 
              </li>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <router-view/>
    <footer class="pt-5">
      <Footer/>
    </footer>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Footer from "@/views/footer/Footer";

export default {
  name: 'App',
  data: function () {
    return {

    }
  },
  components: {
    Footer
  },
  methods: {
    logout () {
      this.$store.commit('deleteToken')
      localStorage.removeItem('accessToken')
      this.$router.push({ name: 'Login' })
    }
  },
  computed: {
    ...mapGetters([
      'isLogin',
      'getUsername'
    ]),
  },
  created () {
    this.$store.dispatch('readMovie')
    this.$store.dispatch('loadMovieCards')
    this.$store.dispatch('loadGenres')
    const accessToken = localStorage.getItem('accessToken') || ''
    this.$store.commit('setToken', accessToken)
  }
}
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #ffffff;
    background-color: #000000;
    font-family: 'Jua', sans-serif;
  }

  #nav {
    padding: 0px;
  }

  #nav a {
    font-weight: bold;
    color: #ffffff;
    -webkit-text-stroke: 0.5px #1d013f;
  }

  .login_active {
    color: #1d013f;
    -webkit-text-stroke: 0.1px white;
    text-shadow : 3px 3px 6px rgb(0, 0, 0);

  }

  .login_user_active {
    color: #ffffff;
    -webkit-text-stroke: 0.1px #1d013f;
  }

  #nav a.router-link-exact-active {
    color: #1d013f;
    font-size: 30px;
    -webkit-text-stroke: 0.5px white;
    text-shadow : 3px 3px 6px rgb(255, 255, 255);
  }

  .back_ground {
    background-color: #00000000;
    z-index: 2;
  }

  .bottom_background {
    background-color: #00000050;
    z-index: 2;
  }

  .img_back_ground {
    background-color: rgba(0, 0, 0, 0, 0, 0);
    margin-left: -30px;
  }

  .menu {
    font-size: 23px;
    text-align:center;
  }

  .login_font {
    font-size: 20px;
    font-weight: bold;
  }

</style>
