<template>
  <div class="box">
    <section>
      <MovieDetailTop/>
    </section>
    <section>
      <ul class="nav nav-tabs navbox">
        <li class="nav-item">
          <router-link id="font_color_active" class="nav-link active text-decoration-none" :to="{ name: 'MovieDetailMain', query: { movieId: $route.query.movieId } }">
            주요정보
          </router-link>
        </li>
        <li class="nav-item">
          <router-link id="font_color" class="nav-link text-decoration-none" :to="{ name: 'MovieDetailCrew', query: { movieId: $route.query.movieId } }">
            출연제작
          </router-link>
        </li>
        <li class="nav-item">
          <router-link id="font_color" class="nav-link text-decoration-none" :to="{ name: 'MovieDetailContents', query: { movieId: $route.query.movieId } }">
            영상/포토
          </router-link>
        </li>
        <li class="nav-item">
          <router-link id="font_color" class="nav-link text-decoration-none" :to="{ name: 'MovieDetailGrade', query: { movieId: $route.query.movieId } }">
            평점
          </router-link>
        </li>
      </ul>
    </section>
    <section class="section_box">
      <p>{{ movieCard.overview }}</p>
    </section>
  </div>
</template>

<script>
import MovieDetailTop from "@/views/detail/MovieDetailTop";
import { mapState } from 'vuex'

export default {
  name: 'MovieDetailMain',

  components: {
    MovieDetailTop,
  },
  computed: {
    ...mapState(['movieCard']),
  },
  created () {
    const movieid = this.$route.query.movieId
    this.$store.dispatch('loadLikeMovie', movieid)
    this.$store.dispatch('loadMovieCard', movieid)
  }
}
</script>

<style scoped>
  .box {
    margin: 0px 200px;
  }
  .section_box {
    margin: 100px 100px;
  }
  .navbox {
    margin: 100px 100px;
  }
  #font_color {
    color: #ffffff;
  }
  #font_color_active {
    color: #000000;
    font-weight: bold;
  }
</style>