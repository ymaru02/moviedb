<template>
  <div class="col" >
    <router-link class="text-decoration-none" :to="{ name: 'MovieDetailMain', query: { movieId: MovieGenreCard.id } }">
      <div 
        id="card_back"
        class="card h-100 border-0 moviecard rounded-3 "
      >
        <img 
          class="rounded-3 h-100"
          :src="`https://image.tmdb.org/t/p/w500${ MovieGenreCard.poster_path }`"
          :alt="`${ MovieGenreCard.id }`"
        >        
      </div>
    </router-link>
  </div>
</template>

<script>

export default {
  name: 'MovieGenreCard',
  props: {
    MovieGenreCard: Object,
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
  },
}
</script>

<style scoped>
  #card_back {
    background-color: #ffffff00;
  }

  .moviecard {
    overflow: hidden;
  }

  .moviecard img {
    object-fit: cover;
    transition: all 0.2s linear;
  }

  .moviecard:hover img {
    transform: scale(1.5);
  }
</style>