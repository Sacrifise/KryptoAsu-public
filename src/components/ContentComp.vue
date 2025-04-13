<template>
    <div class="content-cont">
        <div class="content-cont-calc">
            <div class="content-cont-calc-var">
                <h2>INPUT DATA</h2>
                <form v-if="props.type ==='Nok' || props.type ==='Nod'" class="content-cont-calc-var-form" ref="formSub">
                    <div class="">a = <input type="number" name="a"/></div>
                    <div class="">b = <input type="number" name="b"/></div>
                    <div class="calc-var-form-value" v-for="item, index in variables" :key="index" >{{ item }} = <input :name="item" type="number"/></div>
                </form>

                <form v-if="props.type ==='Abs'" class="content-cont-calc-var-form" ref="formSub">
                    <div class="">a = <input type="number" name="a"/></div>
                    <div class="">b = <input type="number" name="b"/></div>
                    <div class="">c = <input type="number" name="c"/></div>
                </form>

                <div v-if="props.type !='Abs'" class="plus-btn" :class="{ none: isPlusHidden }" @click="createVar()"><img src="../assets/Plus.svg"></div>
            </div>
            <div class="content-cont-calc-result ">
                <div ref="resSub" class="">
                    <span  >Решение: {{ resultData }}</span>
                </div>
                <button @click="submitForm($event)">SOLVE</button>
            </div>
        </div>
        <div class="content-cont-example">
            <div>
                <h2>Example</h2>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref,  watch, defineProps } from 'vue';

const props = defineProps({
    type: String,
    url: String
})

let counter = 99;
const formSub = ref(null)
const resSub = ref(null)
const resultData = ref("");
const variables = ref([]);
const isPlusHidden = ref(false);
const inputData = ref([])

function createVar(){
    variables.value.push(String.fromCharCode(counter))
    counter += 1;
}

function submitForm(e){
    e.preventDefault();
    inputData.value = [];
    formSub.value.querySelectorAll("input").forEach((el) => inputData.value.push(el.value))
    inputData.value = inputData.value.filter((el) => el != "")
    dataPostCall({elements: Array.from(inputData.value)})
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
    console.log(data.result)
    resSub.value.classList.remove("name")
    resultData.value = data.result;
    resSub.value.classList.add("name");
    setTimeout(() => resSub.value.classList.remove("name"), 1000);
    const item = JSON.parse(localStorage.getItem("recent")) || []
    
    item.push(data)
    localStorage.setItem("recent", JSON.stringify(item))
    console.log(localStorage)
}


watch(variables, (newValue) => {
    if (newValue.length >= 6) {
        console.log("POP!");
        isPlusHidden.value = true;
    }
}, { deep: true });

</script>

<style scoped>
    @import './ContentComp.css';
</style>