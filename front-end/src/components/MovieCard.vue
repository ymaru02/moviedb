<template>
  <div class="col" >
    <router-link class="text-decoration-none" :to="{ name: 'MovieDetailMain', query: { movieId: movieCard.id } }">
      <div 
        id="card_back"
        class="card h-100 border-0 moviecard rounded-3 "
        @mouseenter="mouseEnterCard"
        @mouseleave="mouseLeaveCard"
      >
        <img 
          :src="`https://image.tmdb.org/t/p/w500${ movieCard.poster_path }`"
          :alt="`${ movieCard.id }`"
          class="h-75"
        >
        <div 
          class="card-img-overlay overlay_back d-flex justify-content-center"
          v-if="onDetailCard"
        >
          <div class="align-self-center">
            <p class="card-text">
              <span>제목 : </span>  
              <span class="overlay_back_font">{{ movieCard.title }}</span>  
            </p>
            <p class="card-text">
              <span>장르 : </span>  
              <span 
                v-for="genre in movieCard.genres"
                :key="genre.id"
                class="overlay_back_font"
              >
                {{ genre }}
              </span>  
            </p>
            <p class="card-text">
              <span>개봉일 : </span>  
              <span class="overlay_back_font">{{ movieCard.release_date }}</span>  
            </p>
            <p class="card-text">
              <span>상영시간 : </span>  
              <span class="overlay_back_font">{{ movieCard.runtime }}</span>  
              <span>분</span>  
            </p>
            <p class="card-text">
              <span>평점 : </span>  
              <span class="overlay_back_font">{{ movieCard.vote_avg }}</span>  
            </p>
          </div>
        </div>
        <div class="card-body board-none text-white white-space overflow ellipsis rounded-3">
          <h5
            class="card-title text-center title-font rounded-3"
            v-if="!onDetailCard"
          >
            {{ this.movietitle }}
          </h5>
        </div>
        
      </div>
    </router-link>
  </div>
</template>

<script>

export default {
  name: 'MovieCard',
  props: {
    movieCard: Object,
  },
  components: {
  },
  data: function() {
    return {
      onDetailCard: false,
      movietitle: ''
    }
  },
  methods: {
    mouseEnterCard: function () {
      this.onDetailCard = true
    },
    mouseLeaveCard: function () {
      this.onDetailCard = false
    }
  },
  created () {
    this.movietitle = this.movieCard.title.split(':')[0]
  }
}
</script>

<style scoped>
  #card_back {
    background-color: #ffffff00;
  }
  
  .title-font {
    font-size: 15px;
    
  }

  .overlay_back {
    background-color: #252525b6;
    font-size: 15px;
    color: #ffffff;
    -webkit-text-stroke: 0.1px rgb(0, 0, 0);
  }

  .overlay_back_font {
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    -webkit-text-stroke: 0px rgb(0, 0, 0);
  }

  .moviecard {
    margin: 0px auto;
    overflow: hidden;
  }

  .moviecard:hover {
    /* transform: translateY(5px); */
  }

  .moviecard img {
    object-fit: cover;
    transition: all 0.2s linear;
  }

  .moviecard:hover img {
    transform: scale(1.7);
  }
</style>