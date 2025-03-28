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
    dataPostCall({value: Array.from(inputData.value)})
}

async function dataPostCall(content) {
    await fetch(`http://localhost:8000${props.url}`, {
        method: "POST",
        body: JSON.stringify(content),
        headers: {
            "Content-type": "application/json"
        }
    
    
    }).then(res => res.json()).then(json => console.log(json));
    dataGetCall()
}

async function dataGetCall() {
    resSub.value.classList.remove("name")
    try {
        await fetch('http://localhost:8000/GET').then((el) => el.json()).then((e) => {resultData.value = e.results; resSub.value.classList.add("name")});
    } catch (error) {
        console.error('Error:', error);
    }
    setTimeout(() => resSub.value.classList.remove("name"), 1000)
}



watch(variables, (newValue) => {
    if (newValue.length >= 6) {
        console.log("POP!");
        isPlusHidden.value = true;
    }
}, { deep: true });

</script>

<style scoped>
    .name{
        animation: new-result 1s 1 alternate;
        transform-origin: -20% 0;
    }

    .calc-var-form-value{
        animation: birth 1s 1 alternate;
    }
    @keyframes birth {
        from{
            opacity: 0;
            transform: scale(1.4);
        }
        30%{
            opacity: 1;
            transform: scale(1.4) rotate(2deg);
        }
        80%{
            opacity: 1;
            transform: scale(0.9) rotate(-2deg);
        }
        to{
            opacity: 1;
            transform: scale(1) rotate(0deg);
        }
    }
    @keyframes new-result {
        from{
            opacity: 0;
            transform: scale(1.0);
        }
        40%{
            opacity: 1;
            transform: scale(1.1) rotate(-5deg);
        }
        50%{
            opacity: 1;
            transform: scale(1.1) rotate(2.5deg);
        }
        60%{
            opacity: 1;
            transform: scale(1.1) rotate(-2.5deg);
        }
        70%{
            opacity: 1;
            transform: scale(1.1) rotate(1.25deg);
        }
        80%{
            opacity: 1;
            transform: scale(0.9) rotate(-1.25deg);
        }
        to{
            opacity: 1;
            transform: scale(1) rotate(0deg);
        }
    }

    .none{
        display: none !important;
    }
    .plus-btn{
        transition: 0.4s;
        margin-top: 20px;
        width: 60px;
        height: 60px;
        border-radius: 40px;
        background: linear-gradient(90deg, rgba(204,155,255,1) 0%, rgba(214,177,253,1) 100%);
        box-shadow: 0 0 4px 0 rgba(1, 1, 1, 0.25);
        display: flex;
        justify-content: center;
        align-items: center;
        align-self: center;
    }
    .plus-btn img{
        transition: 0.4s;
        width: 60%;
        height: 60%;
    }
    .plus-btn:hover{
        box-shadow: 0 0 20px 0px #d5aaff;
        width: 70px;
        height: 70px;
    }
    .plus-btn:active, .plus-btn:active img{
        transition-duration: 0s;
        filter: brightness(0.9);
    }
    h2, h1, h3{
    font-weight: 400;
    }
    .content-cont-calc-var{
        display: flex;
        flex-direction: column;
        width: 25%;
        height: 90%;
    }
    .content-cont-calc-var form{
        display: flex;
        flex-direction: column;
        gap: 15px;
    }
    .content-cont-calc-var form div{
        height: 2rem;
        color: #676767;
        font-size: 1.7rem;
        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
    }
    .content-cont-calc-var form div input{
        margin-left: 5px;
        height: 1.7rem;
        background-color: #FFFFFF;
        border: 0;
        box-shadow: 0 0 4px 0 rgba(1, 1, 1, 0.25);
        border-radius: 10px;
    }
    .content-cont-calc-result{
        justify-content: space-evenly;
        align-items: center;
        flex-direction: column;
        display: flex;
        height: 90%;
        width: 65%;
    }
    .content-cont-calc-result div{
        box-sizing: border-box;
        display: flex;
        padding: 10px;
        background-color: #FDFDFD;
        width: 90%;
        height: 80%;
        box-shadow: 0 0 4px 0 rgba(1, 1, 1, 0.25);
        border-radius: 30px;
    }
    .content-cont-calc-result button:hover{
        box-shadow: 0 0 20px 0px #d5aaff;
    }
    .content-cont-calc-result button:active{
        filter: brightness(0.9);
        transition-duration: 0s;
    }
    .content-cont-calc-result button{
        transition: 0.4s;
        font-size: 1.2rem;
        color: white;
        align-self: flex-end;
        margin-right: 5%;
        width: 15%;
        height: 10%;
        background: linear-gradient(90deg, rgba(204,155,255,1) 0%, rgba(214,177,253,1) 100%);
        box-shadow: 0 0 4px 0 rgba(1, 1, 1, 0.25);
        border: none;
        border-radius: 30px;
    }
    .content-cont-example{
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #F3F3F3;
        width: 80vw;
        height: 25vh;
        box-shadow: 0 0 4px 0 rgba(1, 1, 1, 0.25);
        border-radius: 30px;
    }
    .content-cont-example div{
        width: 95%;
        height: 90%;
    }
    .content-cont-calc{
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        background-color: #F3F3F3;
        width: 80vw;
        height: 65vh;
        box-shadow: 0 0 4px 0 rgba(1, 1, 1, 0.25);
        border-radius: 30px;
    }
    .content-cont{
        display: flex;
        flex-direction: column;
        width: 85vw;
        justify-content: space-evenly;
        align-items: center;
    }
</style>