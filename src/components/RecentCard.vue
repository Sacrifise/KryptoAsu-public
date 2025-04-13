<template>
    <div class="recent"> 
        <div class="recent-cont">
            <h2>Прошлые Операции</h2>
            <div class="recent-cont-history">
                <div class="history-item" v-for="item, index in results" :key="index">
                    <h3>✔️ {{ index+1 }}:НОД({{ item.value.join(", ") }}) -> </h3> <div class="history-item-text">{{ item.result }}</div>
                </div>
            </div>
            <button @click = "clearStorage()">Отчистить историю</button>
        </div>
    </div>
</template>

<script setup>
import { Text, ref } from 'vue';

function clearStorage(){
    localStorage.setItem("recent", JSON.stringify([]));
    results.value = [];
}
const results = ref([]);

try{
     results.value = JSON.parse(localStorage.getItem("recent")).reverse()
    results.value.forEach((item, index) => console.log(`${index+1}: ${item.result}` ))
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
    box-sizing: border-box;
}
.recent{
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    width: 85vw;
    justify-content: space-evenly;
    align-items: center;
}
.recent-cont-history{
    margin-top: 20px;
    box-sizing: border-box;
    width: 70%;
    max-width: 100%;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    overflow-y: scroll;
    max-height: 65vh;
}
.recent-cont button{
    margin-top: 3rem;
    font-size: 1.2rem;
    color: white;
    width: 20%;
    height: 8%;
    background: linear-gradient(90deg, rgba(204,155,255,1) 0%, rgba(214,177,253,1) 100%);
    box-shadow: 0 0 4px 0 rgba(1, 1, 1, 0.25);
    border: none;
    border-radius: 30px;
    transition: 0.3s;
}
.recent-cont button:hover{
    border-radius: 10px;
}
.recent-cont button:active{
    filter: brightness(0.7);
}
.recent-cont-history::-webkit-scrollbar{
    background-color: rgb(238, 200, 255);
    scrollbar-width: thin;
    border-radius: 10px;
}
.recent-cont-history::-webkit-scrollbar-thumb{
    background-color: #cda2f9;
    border-radius: 10px;
}
.history-item{
    width: 60%;
    align-items: center;
    display: flex;
    border-radius: 10px;
    padding: 10px;
    box-sizing: border-box;
    color: black;
    background-color: white;
    position: relative;
    z-index: 1;
    box-shadow: 0 0px 10px 0 rgba(0, 0, 0, 0.073);
    flex-wrap: wrap;
}



.history-item-text{
    margin: 5px;
    display: flex;
    justify-content: center;
    font-size: 1.3rem;
}
</style>