<template>
  <div v-if="movieCard.back_path" class="cropping" >
    <img 
      :src="`https://image.tmdb.org/t/p/original/${ movieCard.back_path }`" 
      class="d-block w-100 " 
      alt=""
    >
  </div>
</template>

<script>
export default {
  name: 'MovieBackImg',
  props: {
    movieCard: Object
  }
}
</script>

<style scoped>
  .cropping{
    max-height: 800px;
    overflow: hidden;
  }

  .cropping img{
    max-height: initial;
  }
</style>