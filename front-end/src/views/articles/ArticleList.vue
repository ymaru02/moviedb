<template>
  <article>
    <section class="mt-5 pt-5">
      <div class="container">
        <h2 class="float-md-start text-light"> Article List </h2>
        <table class="table table-dark table-striped text-light">
          <thead>
            <tr>
              <th scope="col" class="col-md-1"> No.</th>
              <th scope="col">Title</th>
              <th scope="col" class="col-md-2">Writer</th>
              <th scope="col" class="col-md-3">Created_at</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(article, index) in articles" :index="index" :key="article.id" :article="article">
              <th scope="row">{{ index+1 }}</th>
              <td class=""> 
                <div class="d-flex">
                  <router-link class="text-decoration-none link-dark fw-bold" :to="{ name: 'ArticleDetail', query: { articleId: article.id } }">
                    <h5 class="text-light">{{ article.title }}
                      <span class="badge fs-6 fw-normal">{{ article.comment_count }}</span>
                      <!-- <span class="badge fs-6 fw-normal">{{ review.username }}</span> -->
                    </h5>
                  </router-link>
                </div>
              </td>
              <td>{{ article.username }}</td>
              <td>{{ article.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</td>
            </tr>
          </tbody>
        </table>
        <router-link class="text-decoration-none" :to="{ name: 'ArticleForm'}">
          <button class="btn btn-primary float-end">CREATE</button>
        </router-link>  
      </div>
    </section>
  </article>
</template>

<script>
import Vue from 'vue' 
import vueMoment from 'vue-moment' 
Vue.use(vueMoment)

export default {
  name: 'ArticleList',
  computed: {
    articles () {
      return this.$store.state.articles
    }
  },
  methods: {
    createArticle() {
      this.$router.push({ name: 'ArticleForm' })
    }
  },
  created() {
    this.$store.dispatch('getArticles')
  },
}
</script>

<style scoped>
  .badge {
    background-color: darkslateblue;
  }
</style>
