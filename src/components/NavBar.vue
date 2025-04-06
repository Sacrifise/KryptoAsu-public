<script setup>
import { RouterLink } from 'vue-router';

</script>

<template>
    <div class="navBar-cont">
        <h1 class="navBar-cont-user">CryptoCalc</h1>
        <div class="navBar-cont-routes">
            <h2>Операции</h2>
            
            <RouterLink to="/nok"><div class="text"> <img class="icon" src="../assets/Box.svg">Нок</div></RouterLink>
            <RouterLink to="/nod"><div class="text"> <img class="icon" src="../assets/Octagon.svg">Нод</div></RouterLink>
            <RouterLink to="/abs"><div class="text "> <img class="icon" src="../assets/Cpu.svg">Модуль</div></RouterLink>
            <h2>Шифры</h2>
            <RouterLink to="/atbash"><div class="text"> <img class="icon" src="../assets/Box.svg">Атбаш</div></RouterLink>
            <RouterLink to="/caesar"><div class="text"> <img class="icon" src="../assets/Octagon.svg">Цезарь</div></RouterLink>
            <RouterLink to="/polibius"><div class="text "> <img class="icon" src="../assets/Cpu.svg">Полибий</div></RouterLink>
            <RouterLink to="/shift"><div class="text "> <img class="icon" src="../assets/Cpu.svg">Сдвиг</div></RouterLink>
            <h2>Результаты</h2>
            <RouterLink to="/recent"><div class="text"> <img class="icon" src="../assets/Rotate ccw.svg">История</div></RouterLink>
        </div>
    </div>
</template>

<style scoped>
@import './NavBar.css';
</style>
