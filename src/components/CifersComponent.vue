<script setup>
import { defineProps, ref } from 'vue';
const props = defineProps({
    url: String,
    type: String

})
const ciferForm = ref(null);
const resultForm = ref(null);
const opChoise = ref(null);
const shift = ref(null);


function submitForm(e){
    e.preventDefault();
    if (shift.value)
        dataPostCall({text: ciferForm.value.querySelector("textarea").value, operation: opChoise.value.querySelector('input[name="choise"]:checked').value, shift: shift.value.value});
    else
        dataPostCall({text: ciferForm.value.querySelector("textarea").value, operation: opChoise.value.querySelector('input[name="choise"]:checked').value});

}
async function dataPostCall(content) {
    await fetch(`http://localhost:8000${props.url}`, {
        method: "POST",
        body: JSON.stringify(content),
        headers: {
            "Content-type": "application/json"
        }
    
    
    }).then(res => res.json()).then(json => renderResult(json));
}

async function renderResult(data){
    resultForm.value = data.result;;
    const item = JSON.parse(localStorage.getItem("recent")) || []
    
    item.push(data)
    localStorage.setItem("recent", JSON.stringify(item))
}

</script>

<template>
    <div class="cifers-cont">
        <div class="cifers-cont-item">
            <h2>INPUT DATA</h2>
                <form class="cifers-cont-item-form" ref="ciferForm" @submit="submitForm">
                    <textarea type="text" placeholder="напишите ваш текст здесь"></textarea>
                </form>
            <button class="submit-button" @click="submitForm">submit</button>
            <fieldset ref="opChoise">
                <legend>Выберите тип операции</legend>
                <input type="radio" id="operation-choise1" checked name="choise" value="encryption">
                <label for="operation-choise">Шифровать</label>

                <input type="radio" id="operation-choise2" name="choise" value="decryption">
                <label for="operation-choise2">Дешифровать</label>
            </fieldset>
            <input v-if="props.type === 'Caesar'" placeholder="сдвиг" ref="shift">
        </div>
        <div class="cifers-cont-item">
            <h2>OUTPUT DATA</h2>
            <div>Ответ: {{ resultForm }}</div>
        </div>
    </div>
</template>

<style>
.submit-button{
    margin-top: 1.4rem;
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
.submit-button:hover{
    border-radius: 10px;
}
.submit-button:active{
    filter: brightness(0.7);
}
.cifers-cont-item-form{
    width: 80%;
    height: 24%;
    display: flex;
    justify-content: flex-start;
    flex-direction: column;
    align-items: center;
}
.cifers-cont-item-form textarea{
    padding: 10px;
    box-sizing: border-box;
    height: 100%;
    display: flex;
    width: 100%;
    margin-left: 5px;
    background-color: #FFFFFF;
    border: 0;
    box-shadow: 0 0 4px 0 rgba(1, 1, 1, 0.25);
    border-radius: 10px;
}
.cifers-cont{
    display: flex;
    flex-direction: row;
    width: 85vw;
    justify-content: space-evenly;
    align-items: center;
}
.cifers-cont-item{
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #F3F3F3;
    width: 40vw;
    height: 65vh;
    flex-direction: column;
    box-shadow: 0 0 4px 0 rgba(1, 1, 1, 0.25);
    border-radius: 30px;
}
</style>