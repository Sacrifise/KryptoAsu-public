<script setup>
import ContentComp2 from '../ContentComp2.vue';
import NavBar from '../NavBar.vue';
</script>

<template>
  <div class="window">
    
    <ContentComp2 type="Nod" url="/operations/gcd"/>
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
