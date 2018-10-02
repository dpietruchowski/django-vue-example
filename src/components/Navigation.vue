<template>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <a class="navbar-brand" href="/">{{ name }}</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div v-for="app in apps" class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" :class="{ active: app.name === active_app }" :href="app.href">{{ app.display }}</a>
          </li>
        </ul>
      </div>
    </nav>
</template>

<script>
export default {
    props: {
        name: String,
        apps: Array,
        active_app: String
    },
}
</script>
