<template>
  <div>
    <div class="container-fluid box"
      :class="{box_active : movieCards && searchText}"
    >
    </div>
    <div class="d-flex justify-content-center search_bar w-100">
      <div class="input-group input-group-lg">
        <input @input="search" type="text" class="form-control searchbar_backgroud" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
        <span @click="search" class="input-group-text searchicon_backgroud" id="inputGroup-sizing-lg"><i class="fas fa-search"></i></span>
      </div>
    </div>
    <div class="d-flex flex-wrap find_search rounded-3"
    >
      <div 
        v-for="Card in movieCards"
        :key="Card.id"
      >
        <router-link class="text-decoration-none" :to="{ name: 'MovieDetailMain', query: { movieId: Card.id } }">
          <li class="find_title">{{ Card.title }}</li>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'HomeSearch',
  data: function() {
    return {
      searchText: '',
      movieCards: [],
    }
  },
  computed: {
  },
  methods: {
    // 문자 찾기
    search() {
      this.searchText = document.querySelector(`.input-group input`).value
      if (!this.searchText) {
        this.movieCards = []
        return 
      }
      // 마지막 글자
      let last_char = this.searchText.charAt(this.searchText.length-1);

      // 중성 글자
      let midword = ''
      let index = ((last_char.charCodeAt(0)- 44032) / 28) % 21;
      if(index>=0){
        midword = String.fromCharCode(index + 4449);
      }

      if (midword) {
        this.movieCards = []
        this.$store.state.movieCards.forEach(movieCard => {
          if (movieCard.title.includes(this.searchText)) {
            this.movieCards.push(movieCard)
          }
        })
      }
    },

  },
}
</script>

<style scoped>
  .box {
    display: none;
  }
  .box_active {
    display: flex;
    position: absolute;
    top: 0px;
    padding-bottom: 1000px;
    background: #0000009a;
    z-index: 3;
  }

  .search_bar {
    padding: 0px 300px;
    position: absolute;
    top: 300px;
    z-index: 3;
  }

  .searchbar_backgroud {
    background: #ffffffa4;
    border: none;
    color: #000000;
  }

  .searchicon_backgroud {
    border-color: #000000;
    background: #ffffff49;
    color: #000000;
    border: none;
  }  

  .find_search {
    position: absolute;
    top: 370px;
    margin: 0px 300px;
    padding-bottom: auto;
    z-index: 4;

  }
  .find_title{
    background-color : rgba(0, 0, 0, 0.678);
    color: #ffffff;
    border-radius: 20px;
    margin: 3px 5px;
    padding: 5px 15px;
    font-size: 20px;
  }

  input:focus {
    background: #ffffff;
    outline: 5px solid #11111175;
  }

</style>