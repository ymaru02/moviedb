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
          <router-link id="font_color" class="nav-link text-decoration-none " :to="{ name: 'MovieDetailContents', query: { movieId: $route.query.movieId } }">
            영상/포토
          </router-link>
        </li>
        <li class="nav-item">
          <router-link id="font_color_active" class="nav-link active text-decoration-none " :to="{ name: 'MovieDetailGrade', query: { movieId: $route.query.movieId } }">
            평점
          </router-link>
        </li>
      </ul>
    </section>
    <section>
      <div class="container my-5">
        <div class="card text-dark text-lg-start">
          <div class="card-header fw-bold pt-2">
            네티즌 평점 리스트
          </div>
          <div v-if="movie_reviews.length">
            <ul 
              v-for="review in movie_reviews" 
              class="list-group list-group-flush"
              :key="review.id"
            >
            <div v-if="review">
              <li class="list-group-item">
                <div class="d-flex flex-row justify-content-between">
                  <div class="col-2">
                    <!-- 별점 -->
                    <span class="reviewStar">
                      ★★★★★
                      <span :style="{ width: review.grade * 10 + '%'}">★★★★★</span>
                    </span>
                    <!-- <p class="text-start">({{ review.grade }}점) </p> -->
                  </div>
                  <div class="col-10 d-flex align-items-center">
                    <div class="col-10">
                      <h5>
                        <span class="badge fs-6 fw-normal">{{ review.username }}</span>
                        {{ review.content }}
                      </h5>
                    </div>
                    <div class="col-auto">
                      <div class="d-grid gap-2 d-md-inline">
                        <button v-if="review.username==getUsername" class="btn btn-outline-secondary mx-1" type="button" @click="updateBtn(review.id, review.grade)" data-bs-toggle="modal" data-bs-target="#updateModal">update</button>
                        <button v-if="review.username==getUsername" class="btn btn-outline-danger mx-1" @click="deleteReview(review.id)">delete</button>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
            </div>
            </ul>
          </div>
          <div v-else>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">첫 평점을 평가해주세요.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
    <div class="modal fade text-dark" id="updateModal" tabindex="-1" aria-labelledby="updateModalLabel" data-bs-keyboard="false" data-bs-backdrop="static" aria-hidden="true">
      <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header update-modal">
            <h3 class="modal-title" id="updateModalLabel">{{ movieCard.title }}</h3>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <form @submit="updateReview">
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
                        <span class="updateStar">
                          ★★★★★
                          <span :style="{width:range_per*10 + '%' }">★★★★★</span>
                          <input 
                            name="updateGrade"
                            type="range" 
                            @mousemove="mouseMoveRange"
                            @mouseleave="mouseLeaveRange"
                            @click="mouseclick" 
                            step="1" min="0" max="10"
                          >
                          <div class="fs-5">
                            <label>({{ range_per }}점)</label>
                          </div>
                        </span>
                      </div>
                    </div>
                    <div class="form-floating input-group col-12">
                      <textarea class="form-control rounded-0 mt-2" id="updateTextarea" maxlength="300" style="height:83px;" v-model="review.content" name="content" @input="adjustHeight2"></textarea>
                      <label for="updateTextarea">최대 300자 이내</label>
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
</template>

<script>
import MovieDetailTop from "@/views/detail/MovieDetailTop"
import { mapState, mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  name: 'MovieDetail',

  components: {
    MovieDetailTop,
  },
  data: function() {
    return {
      range_per: 0,
    }
  },
  computed: {
    ...mapState(['movieCard']),
    ...mapState(['review']),
    ...mapGetters(['getUsername']),
    movie_reviews() {
      return _.orderBy(this.movieCard.movie_reviews, 'id', 'desc'); 
    }
  },
  methods: {
    adjustHeight2: function() {
      var textEle = document.querySelector('#updateTextarea')
      textEle.style.height = 'auto'
      var textEleHeight = textEle.scrollHeight
      textEle.style.height = `${textEleHeight + 10}px`
    }, 
    mouseclick: function() {
      const grade = document.querySelector(`.updateStar span`).style.width.replace('%','')
      this.range_per = grade/10
    },
    mouseMoveRange: function(event) {
      const mouse_x = event.clientX - document.querySelector(`.updateStar input`).getBoundingClientRect().left
      const width = document.querySelector(`.updateStar input`).getBoundingClientRect().width
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

      document.querySelector(`.updateStar span`).style.width = `${range_value * 10}%`
    },
    mouseLeaveRange: function() {
      document.querySelector(`.updateStar span`).style.width = `${this.range_per * 10}%`
    },
    deleteReview(reviewId){
      const payload = {
        reviewId: reviewId,
        movieId: this.$route.query.movieId
      } 
      this.$store.dispatch('deleteReview', payload)
    },
    updateBtn(reviewId, reviewGrade){
      this.range_per = reviewGrade
      document.querySelector(`.updateStar span`).style.width = reviewGrade*10+"%"
      this.$store.dispatch('addReview', reviewId)
    },
    updateReview(event) {
      event.preventDefault()
      const targetReview= {
        ...this.review,
        grade: this.range_per,  
        content: event.target[1].value,
      }
      const payload = {
        targetReview: targetReview,
        movieId: this.$route.query.movieId
      } 
      if (targetReview.grade){
        this.$store.dispatch('updateReview', payload)
        document.querySelector('.update-modal > .btn-close').click()
        // this.$store.dispatch('loadMovieCard', this.movieCard.id)
      }else {
        alert("평점을 등록해주세요.\n평점 0점은 등록할 수 없습니다.")
      }
    }
  },
  created () {
    const movieid = this.$route.query.movieId
    this.$store.dispatch('loadMovieCard', movieid)
    this.$store.dispatch('loadLikeMovie', movieid)
  },
}
</script>

<style scoped>
  .box {
    margin: 0px 200px;
  }
  .section_box {
    margin: 100px 100px;
  }
  .navbox {
    margin: 100px 100px;
  }
  .reveiw_padding {
    padding: auto;
  }
  #font_color {
    color: #ffffff;
  }
  .font_center {
    padding: auto;
  }
  #font_color_active {
    color: #000000;
    font-weight: bold;
  }
  #avg_textarea {
    -ms-overflow-style: none; /* IE and Edge */
    scrollbar-width: none; /* Firefox */
  }


  /* 평가 별점 */
    .updateStar {
    position: relative;
    font-size: 2rem;
    color: #ddd;
  }
  
  .updateStar input {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0;
    opacity: 0;
    cursor: pointer;
  }
  
  .updateStar span {
    width: 0;
    position: absolute; 
    left: 0;
    color: red;
    overflow: hidden;
    pointer-events: none;
  }

  .reviewStar {
    position: relative;
    font-size: 30px;
    color: #ddd;
  }

  .reviewStar span {
    position: absolute; 
    left: 0;
    top: -5px;
    color: red;
    overflow: hidden;
    display: flex;
  }
  .badge {
    background-color: #1d013f;
  }
</style>