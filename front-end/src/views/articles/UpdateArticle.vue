<template>
  <article>
    <section class="mt-5 pt-5">
      <div class="container">
        <form class="row mb-3" @submit="updateArticle">
          <label for="validationtitle" class="col-md-2 my-3 col-form-label fw-bold text-light fs-5">Title</label>
          <div class="col-md-10 my-3">
            <input type="text" class="form-control" id="validationtitle" name="title" v-model="article.title" required>
          </div>
          <label for="validationContent" class="col-md-2 my-3 col-form-label fw-bold text-light fs-5">Content</label>
          <div class="col-md-10 my-3">
            <textarea class="form-control" name="content" id="validationContent" v-model="article.content" style="height: 500px" required></textarea>
          </div>
          <button class="btn btn-primary mt-3" type="submit">[SUBMIT]</button>
          <button class="btn btn-secondary my-2" @click="articleList">[BACK]</button>
        </form>
      </div>
    </section>
  </article>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'UpdateArticle',
  computed: {
    ...mapState(['article']),
  },
  methods: {
    articleList(){
      this.$router.push({ name: 'ArticleList' })
    },
    updateArticle (event) {
      event.preventDefault()
      const newArticle= {
        ...this.article,
        title: event.target[0].value,
        content: event.target[1].value,
      }
      this.$store.dispatch('updateArticle', newArticle)
    },
  }
}
</script>
