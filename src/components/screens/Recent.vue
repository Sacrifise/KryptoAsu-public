<script setup>
import ContentComp from '../ContentComp.vue';
import NavBar from '../NavBar.vue';

try{
const results = JSON.parse(localStorage.getItem("recent"))
results.forEach((item) => console.log(`Предыдущий ответ: ${item}`))
}catch(err){
  console.log(err)
}
</script>

<template>
  <div class="window">
    
    <ContentComp type="Recent"/>
    <!-- <div v-for="item, index in results" :key="index">
      Прошлый ответ:{{ item }}
    </div> -->
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
