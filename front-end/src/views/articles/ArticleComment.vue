<template>
  <article>
    <section class="mx-5">
      <div id="bg-comment-movie" class="card text-white border-light text-lg-start">
        <div class="card-header bg-transparent fw-bold pt-2">
          Comments
        </div>
        <div class="container card-body">
          <form @submit="createComment">
            <div class="d-flex flex-row justify-content-between">
              <div class="col-md-10">
                <textarea class="form-control d-inline" name="content" id="validationContent" placeholder="Comments Create" style="height: 100px;" maxlength="300" required></textarea>
              </div>
              <div class="col-md-2">
                <button type="submit" class="btn btn-secondary btn-lg d-inline" style="height:100px;">Comment Submit</button>
              <!-- <div class="col-auto"> -->
              </div>
            </div>
          </form>
        </div>
        <div v-if="article.comment_set" class="container card-body">
          <ul
            v-for="comment in article.comment_set" 
            class="list-group list-group-flush"
            :key="comment.id"
          >
            <div v-if="comment">
              <li class="list-group-item">
                <div class="d-flex flex-row justify-content-between">
                  <div class="col-2">
                    <span class="badge bg-movie fs-6 fw-normal">{{ comment.username }}</span>
                  </div>
                  <div class="col-9">
                    <p class="d-inline mx-2">{{ comment.content }}</p>
                  </div>
                  <div class="col-auto">
                    <div class="d-grid gap-2 d-md-inline">
                      <button v-if="comment.username == getUsername" type="button" class="btn-close" aria-label="Close" @click="deleteComment(comment.id)"></button>
                    </div>
                  </div>
                </div>
                <div>
                  <div>
                    <p class="card-text"><small class="text-muted">{{ comment.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</small></p>
                  </div>
                </div>
              </li>
            </div>
          </ul>
        </div>
        <div v-else>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">첫 댓글을 작성해주세요.</li>
          </ul>
        </div>
      </div>
    </section>
  </article>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import Vue from 'vue' 
import vueMoment from 'vue-moment' 

Vue.use(vueMoment)

export default {
  name: 'ArticleComment',
  computed: {
    ...mapState(['article']),
    ...mapState(['comment']),
    ...mapGetters(['getUsername']),
  },
  methods: {
    createComment (event) {
      event.preventDefault()
      const newComment= {
        article_id: this.article.id,
        content: event.target[0].value,
      }
      const payload = {
        newComment: newComment,
        articleId: this.article.id
      }
      this.$store.dispatch('createComment', payload)
      event.target[0].value = ''
    },
    deleteComment (commentId){
      const payload = {
        commentId: commentId,
        articleId: this.article.id
      }
      this.$store.dispatch('deleteComment', payload)
    },
  },
}
</script>
<style scoped>
  #bg-comment-movie {
    background-color: #000000;
  }
  .badge {
    background-color: #1d013f;
  }
</style>

