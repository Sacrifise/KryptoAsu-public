<script setup>
import { RouterLink, RouterView } from 'vue-router';
import ContentComp from './components/ContentComp.vue';
import NavBar from './components/NavBar.vue';
</script>

<template>
  <div class="window">
    <NavBar/>
    <RouterView></RouterView>
  </div>
</template>

<style scoped>

.window{
  font-family: "Montserrat", sans-serif;
  font-weight: 500;
  background-color: #D9D9D9;
  justify-content: flex-start;
  padding: 0;
  margin: 0;
  display: flex;
  width: 100vw;
  height: 100vh;
}
</style>
