<script setup>
import CifersComponent from '../CifersComponent.vue';
</script>

<template>
  <div class="window">
    
    <CifersComponent type="Caesar" url="/operations/cifers/caesar"/>
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
