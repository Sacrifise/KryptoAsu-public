<template>
    <div class="recent"> 
        <div class="recent-cont">
            <h2>Прошлые Операции</h2>
            <div class="recent-cont-history">
                <div class="history-item" v-for="item, index in results" :key="index">
                    <h3>{{ index+1 }}: Ответ</h3> <div class="history-item-text">{{ item }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { Text } from 'vue';


let results;
try{
     results = JSON.parse(localStorage.getItem("recent")).reverse()
    results.forEach((item, index) => console.log(`${index+1}: ${item}` ))
}catch(err){
  console.log(err)
}

</script>

<style scoped>
.recent-cont{
    flex-direction: column;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #F3F3F3;
    width: 80vw;
    height: 90vh;
    box-shadow: 0 0 4px 0 rgba(1, 1, 1, 0.25);
    border-radius: 30px;
}
.recent{
    display: flex;
    flex-direction: column;
    width: 85vw;
    justify-content: space-evenly;
    align-items: center;
}
.recent-cont-history{
    margin-top: 20px;
    box-sizing: border-box;
    width: auto;
    min-width: 15%;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.history-item{
    align-items: center;
    display: flex;
    border-radius: 25px;
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
    color: white;
    background-color: #ffacdb;
    position: relative;
    z-index: 1;
    box-shadow: 0 5px 0 0 rgb(255, 155, 212);
    transition: 0.3s;
}
.history-item:hover{
    box-shadow: 0 8px 0 0 #debcff;
    background-color: #cd9bff;
}


.history-item-text{
    margin: 5px;
    width: 75%;
    display: flex;
    justify-content: center;
    font-size: 1.3rem;
}
</style>