<template>
  <div>
    <section>
      <HomeMain/>
    </section>
    <section>
      <!-- <HomeSearch/> -->
      <HomeRecommend
        v-if="getRecommend.length"
        :genres="getRecommend"
      />
    </section>
      <section
      v-for="genre in getGenrePick"
      :key="genre.id"
    >
      <HomeAlgorithm
        :genre="genre"
      />
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
import HomeMain from '@/views/homes/HomeMain'
// import HomeSearch from '@/views/homes/HomeSearch'
import HomeAlgorithm from '@/views/homes/HomeAlgorithm'
import HomeRecommend from '@/views/homes/HomeRecommend'
import { mapGetters, mapState } from 'vuex'
// import _ from 'lodash'

export default {
  name: 'Home',
  components: {
    HomeMain,
    // HomeSearch,
    HomeAlgorithm,
    HomeRecommend,
  },
  computed: {
    ...mapGetters(['getGenrePick']),
    ...mapState(['movieLikes']),
    ...mapGetters(['getRecommend']),
  },
  created () {
    this.$store.dispatch('loadLikeMovies')
  }
}
</script>

<style>


</style>