<template>
  <div id="carouselExampleSlidesOnly" class="carousel slide carousel_background"  data-bs-ride="carousel">
    <div class="carousel-inner">
      <MovieBackImg
        v-for="movieCard in randomBackGroundPick"
        :key="movieCard.id"
        :movieCard="movieCard"
        class="carousel-item"
        :class="{ active: randomBackGroundPick[0] == movieCard }"
        data-bs-interval="2000"
      />
    </div>
    <div>
      <HomeSearch/>
    </div>
    <div id="carouselExampleControls" class="carousel slide carousel_card" data-bs-ride="carousel">
      <div class="carousel-inner" >
      <div
        v-for="(movieCardList, index) in randomGroupCardsPick"
        :key="index"  
        class="carousel-item" data-bs-interval="20000"
        :class="{ active: randomGroupCardsPick[0] == movieCardList }"
      >
        <div class="row row-cols-md-3 row-cols-lg-5 g-4">
          <MovieCard
            v-for="movieCard in movieCardList"
            :key="movieCard.id"
            :movieCard="movieCard"
          />
        </div>
      </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
import HomeSearch from '@/views/homes/HomeSearch'
import MovieCard from '@/components/MovieCard'
import MovieBackImg from '@/components/MovieBackImg'
import _ from 'lodash'

import { mapState } from 'vuex'

export default {
  name: 'HomeMain',
  components: {
    MovieCard,
    MovieBackImg,
    HomeSearch,
  },
  computed: {
    ...mapState(['movieCards']),
    ...mapState(['movieCardArray']),
    randomBackGroundPick: function () {
      return _.sampleSize(this.$store.state.movieCards, 20)
    },
    randomGroupCardsPick: function () {
      const movieCardArray = []
      for (let index = 0; index < 20 / 5; index++) {
        movieCardArray.push(_.sampleSize(this.$store.state.movieCards, 100).slice(index * 5, (index + 1) * 5))
      }
      return _.sampleSize(movieCardArray, 10)
    },
  },
  props: {
    genres: Array
  },
  methods: {
  },
}
</script>

<style scoped>
  .carousel_background{
    position: relative;
    top: -80px;
    margin-bottom: -300px;
    z-index: 1;
  }

  .carousel_card {
    position: relative;
    bottom: 330px;
    padding: 0px 150px;
    z-index: 2;
  }

  .carousel_card_inner {
    bottom: 330px;
    padding: 0px 150px;
  }

  .button_left {
    margin-left: -10px;
  }

  .button_right {
    margin-right: -10px;
  }
</style>