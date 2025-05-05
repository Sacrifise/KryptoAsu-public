<script setup>
import { ref,  watch, defineProps } from 'vue';

const props = defineProps({
    type: String,
    url: String
})


const formSub = ref(null)
const resSub = ref(null)
const resultData = ref("");
const variables = ref([]);
const isPlusHidden = ref(false);
const inputData = ref([])
let counter = 99;
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
    resSub.value.classList.remove("name")
    resultData.value = data;
    resSub.value.classList.add("name");
    setTimeout(() => resSub.value.classList.remove("name"), 1000);
    const item = JSON.parse(localStorage.getItem("recent")) || []
    item.push(data)
    localStorage.setItem("recent", JSON.stringify(item))
}


watch(variables, (newValue) => {
    if (newValue.length >= 6) {
        isPlusHidden.value = true;
    }
}, { deep: true });

</script>

<template>
    <div class="content-cont">
        <div class="content-cont-calc">
            <div class="content-cont-calc-var">
                <h2>INPUT DATA</h2>
                <form v-if="props.type ==='Nok' || props.type ==='Nod'" class="content-cont-calc-var-form" ref="formSub">
                    <div class=""><span>a =</span><input type="number" name="a" placeholder="Введите число"/></div>
                    <div class=""><span>b =</span><input type="number" name="b" placeholder="Введите число"/></div>
                    <div class="calc-var-form-value" v-for="item, index in variables" :key="index" ><span>{{ item }} = </span><input :name="item" type="number" placeholder="Введите число"/></div>
                </form>

                <form v-if="props.type ==='Abs'" class="content-cont-calc-var-form" ref="formSub">
                    <div class=""><span>a =</span><input type="number" placeholder="Введите число" name="a"/></div>
                    <div class=""><span>b =</span><input type="number" placeholder="Введите число" name="b"/></div>
                    <div class=""><span>c =</span><input type="number" placeholder="Введите число" name="c"/></div>
                </form>

                <div v-if="props.type !='Abs'" class="plus-btn" :class="{ none: isPlusHidden }" @click="createVar()"><img src="../assets/Plus.svg"></div>
                <div class="submit-area">
                    <button @click="submitForm($event)" class="submit-btn">SOLVE</button>
                </div>
            </div>
            <div class="content-cont-calc-result ">
                <div ref="resSub" class="">
                    
                        <span>{{ resultData.result ? resultData.result : "null" }}</span>
                        <h3 v-if="props.type == 'Nod'">Наибольший общий делитель</h3>
                        <h3 v-if="props.type == 'Nok'">Наименьшее общее кратное</h3>
                        <h3 v-if="props.type == 'Abs'">Сравнения по модулю</h3>
                        <h3>{{ resultData.type }}({{ resultData.value }})  {{ " => " + (resultData.result ? resultData.result: "null") }}</h3>
                    
                </div>
                
            </div>
        </div>
        <div class="content-cont-example">
            <div class="content-cont-example-area">
                <h2>Example</h2>
                    <div class="content-cont-example-grid">
                        <div class="grid-item">
                            <h3>Базовый пример Нод:</h3> <div>Easy</div><br>
                            <p>Шаги для чисел 48 и 18:<br>
                                Делим 48 на 18:<br>
                                48 ÷ 18 = 2 (остаток 12).<br>
                                Теперь ищем НОД(18, 12).<br>
                                Делим 18 на 12:<br>
                                18 ÷ 12 = 1 (остаток 6).<br>
                                Теперь ищем НОД(12, 6).<br>
                                Делим 12 на 6:<br>
                                12 ÷ 6 = 2 (остаток 0).<br>
                                Остаток 0, значит, НОД = 6.<br>
                                Итог: НОД(48, 18) = 6.<br>
                            </p>
                        </div>
                        <div class="grid-item">
                            <h3>Базовый пример Нок:</h3> <div>Easy</div><br>
                            <h3>Пример для трёх чисел (НОК 6, 8, 12)
                                Разложим на множители:<br>
                                6 = 2 × 3<br>
                                8 = 2³<br>
                                12 = 2² × 3<br>
                                Выберем максимальные степени:<br>
                                Двойка: 2³ (из 8).<br>
                                Тройка: 3¹ (из 6 и 12).<br>
                                Перемножим:<br>
                                НОК = 2³ × 3 = 8 × 3 = 24.<br>
                            </h3>
                        </div>
                        <div class="grid-item">
                            <h3>Базовый пример Уравнений сравнений по модулю:</h3><div style="color: #8e913d; background-color: #fcffae;">Medium</div><br>
                            <h3>Пример для 4x≡8(mod12)<br>
                                Уравнение: 4x≡8(mod12)<br>
                                Проверка: НОД(4, 12) = 4. 4 делит 8 → решение есть.<br>
                                Упрощение: Делим на 4:<br>
                                x≡2(mod3)<br>
                                Общее решение:<br>
                                x=2+3k,k∈Z<br>
                                Конкретные решения (mod 12):<br>
                                x≡2,5,8,11(mod12)<br>
                            </h3>
                        </div>
                        <div class="grid-item">
                            <h3>Базовый пример Шифрования Атбаш:</h3><div style="color: #8e913d; background-color: #fcffae;">Medium</div><br>
                            <h3>Пример для слова "HELLO"<br>
                                Зашифруем слово "HELLO":<br>
                                H ↔ S<br>
                                E ↔ V<br>
                                L ↔ O (дважды)<br>
                                O ↔ L<br>
                                Результат: "SVOOL".<br>
                            </h3>
                        </div>
                    </div>
                
                
            </div>
        </div>
    </div>
</template>

<style scoped>
    @import './ContentComp2.css';
</style>