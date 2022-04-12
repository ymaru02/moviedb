<template>
  <div class="container">
    <div class="row justify-content-start">
      <div class="col-4 ">
        <img v-if="movieCard.poster_path" :src="`https://image.tmdb.org/t/p/w500${ movieCard.poster_path }`" class="d-block w-75 rounded-3" alt="">
      </div>
      <div class="col-8 text-start text-white">
        <div class="detail_title">
          <h1>{{ movieCard.title }}</h1>
        </div>
        <div class="">
          <p>
            <span class="tab">개봉 :&#9;</span>
            <span>{{ movieCard.release_date }}</span>
          </p>
          <p>
            <span class="tab">장르 :&#9;</span>
            <span 
              v-for="genre in movieCard.genres"
              :key="genre.id"
            >
              {{ genre.name }}
            </span>
          </p>
          <p>
            <span class="tab">국가 :&#9;</span>
            <span>{{ movieCard.production_country }}</span>
          </p>
          <p>
            <span class="tab">러닝타임 :&#9;</span>
            <span>{{ movieCard.runtime }} 분</span>
          </p>
          <p>
            <span class="tab">평점 :&#9;</span>
            <span>{{ movieCard.vote_avg }}</span>
          </p>
        </div>
        <div>
          <button v-if="!getWriteReview" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            평가하기
          </button>
          <button v-if="!movieLike" type="button" class="btn btn-primary" @click="like_movie">
            좋아요
          </button>
          <button v-if="movieLike" type="button" class="btn btn-primary" @click="like_movie">
            좋아요 취소
          </button>

          <!-- Modal -->
          <div class="modal fade text-dark" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" data-bs-keyboard="false" data-bs-backdrop="static" aria-hidden="true">
            <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
              <div class="modal-content">
                <div class="modal-header">
                  <h3 class="modal-title" id="exampleModalLabel">{{ movieCard.title }}</h3>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form @submit="createReview">
                  <div class="modal-body">
                    <section>
                      <div class="container">
                        <span>네티즌 평점</span>
                        <span>{{movieCard.vote_avg}} 점</span>
                        <span>( {{movieCard.vote_count}} )</span>
                        <div class="row">
                          <div class="col-12 ">
                            <div class="p-3 bg-light">
                              <!-- 별점 -->
                              <span class="star">
                                ★★★★★
                                <span>★★★★★</span>
                                <input 
                                  name="grade"
                                  type="range" 
                                  @mousemove="mouseMoveRange"
                                  @mouseleave="mouseLeaveRange"
                                  @click="mouseclick" 
                                  step="1" min="0" max="10"
                                >
                                <div class="fs-5">
                                  <label>({{range_per}}점)</label>
                                </div>
                              </span>
                            </div>
                          </div>
                          <div class="form-floating input-group col-12">
                            <textarea class="form-control rounded-0 mt-2" id="floatingTextarea2" maxlength="300" style="height:83px;" name="content" @input="adjustHeight"></textarea>
                            <label for="floatingTextarea2">최대 300자 이내</label>
                          </div>
                        </div>
                      </div>
                    </section>
                  </div>
                  <div class="modal-footer">
                    <div class="p-3 bg-light text-start">
                      ※ 이 평가에 대한 법적 책임은 작성자에게 귀속됩니다.
                    </div>
                    <button type="submit" class="btn btn-primary">Save Review</button>
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
// import _ from 'lodash'

export default {
  name: 'MovieDetailTop',
  data : function() {
    return {
      range_per: 0,
    }
  },
  computed: {
    ...mapState(['movieCard']),
    ...mapState(['movieLike']),
    ...mapGetters(['getUsername']),
    ...mapGetters(['getWriteReview']),
  },
  methods: {
    adjustHeight: function() {
      var textEle = document.querySelector('textarea')
      textEle.style.height = 'auto'
      var textEleHeight = textEle.scrollHeight
      textEle.style.height = `${textEleHeight + 10}px`
    }, 

    // 평가하기
    mouseclick: function() {
      const grade = document.querySelector(`.star span`).style.width.replace('%','')
      this.range_per = grade/10
    },
    mouseMoveRange: function(event) {
      const mouse_x = event.clientX - document.querySelector(`.star input`).getBoundingClientRect().left
      const width = document.querySelector(`.star input`).getBoundingClientRect().width
      let range_value = 0

      if (mouse_x / width > 0.9) {
        range_value = 10;
      } else if (mouse_x / width > 0.8){
        range_value = 9;
      } else if (mouse_x / width > 0.7){
        range_value = 8;
      } else if (mouse_x / width > 0.6){
        range_value = 7;
      } else if (mouse_x / width > 0.5){
        range_value = 6;
      } else if (mouse_x / width > 0.4){
        range_value = 5;
      } else if (mouse_x / width > 0.3){
        range_value = 4;
      } else if (mouse_x / width > 0.2){
        range_value = 3;
      } else if (mouse_x / width > 0.1){
        range_value = 2;
      } else if (mouse_x / width > 0){
        range_value = 1;
      } else {
        range_value = 0;
      }

      document.querySelector(`.star span`).style.width = `${range_value * 10}%`
    },
    mouseLeaveRange: function() {
      document.querySelector(`.star span`).style.width = `${this.range_per * 10}%`
    },
    createReview (event) {
      event.preventDefault()
      const newReview= {
        movie_id: this.movieCard.id,
        grade: this.range_per,  
        content: event.target[1].value,
      } 
      const payload = {
        newReview: newReview,
        movieId: this.movieCard.id,
      }
      if (newReview.grade){
        this.$store.dispatch('createReview', payload)
        document.querySelector('.btn-close').click()
      }else {
        alert("평점을 등록해주세요.\n평점 0점은 등록할 수 없습니다.")
      }
    },

    // 좋아요
    like_movie: function () {
      this.$store.dispatch('updateLikeMovie', this.movieCard.id)
    }
  },
  created () {
    this.$store.dispatch('loadLikeMovies')
  }
}
</script>

<style scoped>
  h1 {
    margin: 30px 0px;
  }

  button {
    margin-right: 15px;
  }

  .tab {
    white-space: pre; 
  }
  .detail_title {
    font-size: 14px;
    line-height: 1.5;
  }

    /* 평가 별점 */
  .star {
    position: relative;
    font-size: 2rem;
    color: #ddd;
  }
  
  .star input {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0;
    opacity: 0;
    cursor: pointer;
  }
  
  .star span {
    width: 0;
    position: absolute; 
    left: 0;
    color: red;
    overflow: hidden;
    pointer-events: none;
  }


</style>