<template>
  <div>
    <h1>{{ this.getUsername }} 님을 위한 추천 영화</h1>
    <div id="carouselExampleControlsrecommend" class="carousel slide carousel-card" data-bs-ride="carousel">
      <div class="carousel-inner">
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
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControlsrecommend" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControlsrecommend" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
import MovieGenreCard from '@/components/MovieGenreCard'
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'HomeRecommend',
  data: function () {
    return {
      movieCardsArray: []
    }
  },
  components: {
    MovieGenreCard,
  },
  computed: {
    ...mapGetters(['getUsername']),
  },
  props: {
    genres: Array,
  },
  created () {
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
      console.log(this.movieCardsArray)
  }
} 
</script>

<style scoped>
  .carousel-card {
    padding: 0px 150px;
  }

  .button-padding {
    padding: 150px 0px 150px 0px;
  }
</style>