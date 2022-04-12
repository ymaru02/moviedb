<template>
  <article>
    <section class="my-3 mx-5">
      <div class="container">
        <div id="bg-movie" class="card text-white text-center border-light text-lg-start">
          <div class="card-header">
            <h4>Detail</h4>
          </div>
          <div class="card-body d-flex justify-content-start">
            <div class="col-12 flex-column">
              <h5 class="card-title">Title : {{ article.title }}</h5>
              <p class="card-text">Writer : {{ article.username }}</p>
              <pre id="pre-view" class="card-text text-lg-start"><h6>Content : {{ article.content }}</h6></pre>
              <p class="card-text text-lg-end">Created_at : {{ article.created_at | moment('YYYY-MM-DD HH:mm:ss')}}</p>
              <p class="card-text text-lg-end">Updated_at : {{ article.updated_at | moment('YYYY-MM-DD HH:mm:ss')}}</p>
              <button v-if=" article.username === this.getUsername" class="btn btn-danger my-4 mx-2 float-end" @click="deleteArticle">DELETE</button>
              <button class="btn btn-secondary my-4 mx-2 float-end" @click="articleList">BACK</button>
              <button v-if=" article.username === this.getUsername" class="btn btn-success my-4 mx-2 float-end" @click="updateArticle">UPDATE</button>
            </div>
          </div>
          <div class="card-footer text-muted">
            <ArticleComment/>
          </div>
        </div>
      </div>
    </section>
  </article>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import Vue from 'vue' 
import vueMoment from 'vue-moment' 
import ArticleComment from '@/views/articles/ArticleComment'

Vue.use(vueMoment)

export default {
  name: 'ArticleDetail',
  computed: {
    ...mapState(['article']),
    ...mapState(['comment']),
    ...mapGetters(['getUsername']),
  },
  components: {
    ArticleComment,
  },
  methods: {
    articleList(){
      this.$router.push({ name: 'ArticleList' })
    },
    deleteArticle(){
      this.$store.dispatch('deleteArticle', this.article)
    },
    updateArticle(){
      this.$router.push({ name: 'UpdateArticle', query: { articleId: this.article.id }})
    },
  },
  created () {
    const articleid = this.$route.query.articleId
    this.$store.dispatch('loadArticleDetail', articleid)
  }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

  #pre-view{
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #ffffff;
    background-color: #000000;
    font-family: 'Jua', sans-serif;
  }

  #bg-movie {
    background-color: #000000;
  }
</style>

