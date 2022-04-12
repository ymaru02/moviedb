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
          <router-link id="font_color" class="nav-link text-decoration-none " :to="{ name: 'MovieDetailCrew', query: { movieId: $route.query.movieId } }">
            출연제작
          </router-link>
        </li>
        <li class="nav-item">
          <router-link id="font_color_active" class="nav-link active text-decoration-none " :to="{ name: 'MovieDetailContents', query: { movieId: $route.query.movieId } }">
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
    <section>
      <!-- Youtube
         https://stackoverflow.com/questions/58489796/how-to-set-samesite-cookie-for-youtube-in-laravel-5-8 -->
      <iframe  v-on:resize="handleResize" :src="`https://www.youtube.com/embed/${movieCard.video_key}?&autoplay=1`" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen :width="this.width" :height="this.height" controls autoplay></iframe>
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
    return {
      width: window.innerWidth * 0.8,
      height: window.innerHeight * 0.8
    }
  },
  computed: {
    ...mapState(['movieCard']),
  },
  mounted() {
    // console.log("ready...");
    window.addEventListener('resize', this.handleResize);
	},
  beforeDestroy() {
    // console.log("beforeDestroy...");
    window.removeEventListener('resize', this.handleResize);
  },
  // updated() {
  //   window.addEventListener('resize', this.handleResize);
  // },
  methods: {
    handleResize() {
      this.width = window.innerWidth * 0.7;
      this.height = window.innerHeight * 0.8;
    }
  },
  created () {
    const movieid = this.$route.query.movieId
    this.$store.dispatch('loadMovieCard', movieid)
    this.$store.dispatch('loadLikeMovie', movieid)
  }
}
</script>

<style scoped>
  .box {
    margin: 0px 200px;
  }
  /* .section_box {
    margin: 0px 100px;
  } */
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