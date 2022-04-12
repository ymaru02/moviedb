<template>
<div>
  <h1>{{ this.genre.name }}</h1>
  <div :id="`carouselExampleControls${this.genre.id}`" class="carousel slide carousel-card" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div
        v-for="(movieCardList, index) in movieCardsArray"
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
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" :data-bs-target="`#carouselExampleControls${this.genre.id}`" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" :data-bs-target="`#carouselExampleControls${this.genre.id}`" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</div>
</template>

<script>
// import _ from 'lodash'
import axios from 'axios'
import MovieGenreCard from '@/components/MovieGenreCard'

export default {
  name: 'HomeAlgorithm',
  components: {
    MovieGenreCard,
  },
  props: {
    genre: Object,
  },
  data: function() {
    return {
      movieCardsArray: [],
    }
  },
  created () {
    axios.get(`http://127.0.0.1:8000/movies/${ this.genre.id }/genre/movie/`)
    .then((res) => {
      for (let index = 0; index < res.data.length / 5; index++) {
        this.movieCardsArray.push(res.data.slice(index * 5, (index + 1) * 5))
      }
    })
  }
}
</script>

<style scoped>

  h1 {
    margin-top: 50px;
  }
  .carousel-card {
    padding: 0px 150px;
  }

  .button-padding {
    padding: 150px 0px 150px 0px;
  }
</style>