<template>
  <div class="container">
    <!--    <h1 v-if="error.statusCode === 404">Page not found</h1>-->
    <!--    <h1 v-else>An error occurred</h1>-->
    <!--    <nuxt-link to="/">Home page</nuxt-link>-->
  </div>
</template>

<script>
export default {
  props: ['error'],
  // layout: 'blog', // you can set a custom layout for the error page
  created() {
    console.log(this.error)
    if (this.error.statusCode === 404) {
      setTimeout(() => {
        this.$router.push('/')
      }, 1)
    }
  }
}
</script>
