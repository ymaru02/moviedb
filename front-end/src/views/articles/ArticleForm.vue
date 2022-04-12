<template>
  <article>
    <section class="mt-5 pt-5">
      <div class="container">
        <form class="row mb-3" @submit="createArticle">
          <div class="col-md-2 my-3">
            <label for="validationtitle" class="col-md-2 col-form-label fw-bold text-light fs-5">Title</label>
          </div>
          <div class="col-md-10 my-3">
            <input type="text" class="form-control" id="validationtitle" name="title" required>
          </div>
          <div class="col-md-2 my-3">
            <label for="validationContent" class="col-md-2 col-form-label fw-bold text-light fs-5">Content</label>
          </div>
          <div class="col-md-10 my-3">
            <textarea class="form-control" name="content" id="validationContent" style="height: 400px" required></textarea>
          </div>
          <div class="col-12">
            <button class="btn btn-secondary float-end" @click="articleList">BACK</button>
            <button class="btn btn-primary float-end mx-2" type="submit">SUBMIT</button>
          </div>
        </form>
      </div>
    </section>
  </article>
</template>

<script>
export default {
  name: 'ArticleForm',
  methods: {
    createArticle (event) {
      event.preventDefault()
      const newArticle= {
        title: event.target[0].value,
        content: event.target[1].value,
      }
      this.$store.dispatch('createArticle', newArticle)
    },
    articleList(){
      this.$router.push({ name: 'ArticleList' })
    }
  }
}
</script>
