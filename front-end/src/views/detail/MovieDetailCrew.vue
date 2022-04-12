<template>
  <div class="box">
    <section>
      <MovieDetailTop/>
    </section>
    <section>
      <ul class="nav nav-tabs navbox">
        <li class="nav-item">
          <router-link id="font_color" class="nav-link text-decoration-none " :to="{ name: 'MovieDetailMain', query: { movieId: $route.query.movieId } }">
            주요정보
          </router-link>
        </li>
        <li class="nav-item">
          <router-link id="font_color_active" class="nav-link active text-decoration-none " :to="{ name: 'MovieDetailCrew', query: { movieId: $route.query.movieId } }">
            출연제작
          </router-link>
        </li>
        <li class="nav-item">
          <router-link id="font_color" class="nav-link text-decoration-none " :to="{ name: 'MovieDetailContents', query: { movieId: $route.query.movieId } }">
            영상/포토
          </router-link>
        </li>
        <li class="nav-item">
          <router-link id="font_color" class="nav-link text-decoration-none " :to="{ name: 'MovieDetailGrade', query: { movieId: $route.query.movieId } }">
            평점
          </router-link>
        </li>
      </ul>
    </section>
    <section v-if="movieCard" class="section_box">
      <h5>Actors</h5>
      <hr>
      <div class="row row-cols-2 row-cols-md-3 row-cols-lg-4 g-1">
        <div 
          class="col"
          v-for="actor in getfristActor"
          :key="actor.id"
        >
          <div id="card_back" class="card mb-3" style="max-width: 540px;">
            <div class="row g-0">
              <div class="col-md-4" v-if="actor.actor.profile_path">
                <img :src="`https://image.tmdb.org/t/p/w500${ actor.actor.profile_path }`" class="img-fluid rounded-start rounded-3" alt="...">
              </div>
              <div class="col-md-4" v-else>
                <img src="@/assets/logo.png" class="img-fluid rounded-start rounded-3" alt="...">
              </div>
              <div class="col-md-8">
                <div class="card-body" v-if="actor.actor.name">
                  <p class="card-title profile_font">{{ actor.actor.name }}</p>
                  <p class="card-title profile_role_font">{{ actor.character }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button @click="addActor" type="button"
      :class="{ nonebutton: count_actor <= movie_actor }"
       class="btn btn-dark addbutton"><i class="fas fa-user-plus"></i></button>

      <h5>Crews</h5>
      <hr class="hr">
      <div class="row row-cols-2 row-cols-md-3 row-cols-lg-4 g-1">
        <div 
          class="col"
          v-for="crew in getfristCrew"
          :key="crew.id"
        >
          <div id="card_back" class="card mb-3" style="max-width: 540px;">
            <div class="row g-0">
              <div class="col-md-4" v-if="crew.crew.profile_path">
                <img :src="`https://image.tmdb.org/t/p/w500${ crew.crew.profile_path }`" class="img-fluid rounded-start rounded-3" alt="...">
              </div>
              <div class="col-md-4" v-else>
                <img src="@/assets/logo.png" class="img-fluid rounded-start rounded-3" alt="...">
              </div>
              <div class="col-md-8">
                <div class="card-body" v-if="crew.crew.name">
                  <p class="card-title profile_font">{{ crew.crew.name }}</p>
                  <p class="card-title profile_role_font">{{ crew.department }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button @click="addCrew" type="button" 
      :class="{nonebutton: count_crew <= movie_crew }"
      class="btn btn-dark addbutton"><i class="fas fa-user-plus"></i></button>
    </section>
  </div>
</template>

<script>
import MovieDetailTop from "@/views/detail/MovieDetailTop";
import { mapState } from 'vuex'

export default {
  name: 'MovieDetail',

  components: {
    MovieDetailTop,
  },
  data: function () {
    return{
      movie_actor: 12,
      movie_crew: 12,
      count_actor: 13,
      count_crew: 13,
    }
  },
  computed: {
    ...mapState(['movieCard']),
    getfristActor() {
      if (!this.movieCard.movie_actors) return
      return this.movieCard.movie_actors.slice(0, this.movie_actor)
   },
    getfristCrew() {
      if (!this.movieCard.movie_crews) return
      return this.movieCard.movie_crews.slice(0, this.movie_crew)
    },
  },
  methods: {
    addActor: function() {
      this.count_actor = this.movieCard.movie_actors.lenght,
      this.movie_actor += 12
    },
    addCrew: function() {
      this.count_crew = this.movieCard.movie_crews.lenght,
      this.movie_crew += 12
    },
  },
  created () {
    const movieid = this.$route.query.movieId
    this.$store.dispatch('loadMovieCard', movieid)
    this.$store.dispatch('loadLikeMovie', movieid)
  }
}
</script>

<style scoped>

  hr {
    border: solid 1px #ffffff;
    color: #ffffff;
    background-color:#ffffff;
  }

  .addbutton {
    margin-bottom: 50px;
  }
  
  .nonebutton{
    display: none;
  }

  #font_color {
    color: #ffffff;
  }
  #font_color_active {
    color: #000000;
    font-weight: bold;
  }
  #card_back {
    background-color: #000000;
  }

  .box {
    margin: 0px 200px;
    background-color: #000000;
  }
  .navbox {
    margin: 100px 100px;
  }
  .section_box {
    margin: 100px 100px;
  }
  .profile_font {
    font-size: 12px;
  }
  .profile_role_font {
    font-size: 8px;
    color: #8f8f8f;
  }

</style>