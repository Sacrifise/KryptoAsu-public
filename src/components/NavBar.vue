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
.navBar-cont-user::after{
    content: "CryptoCalc";
    color: #8958BE;
    position: absolute;
    top: 2.5px;
    left: 0px;
    z-index: -1;
    transition: 0.2s;

}
.navBar-cont-user::before{
    content: "CryptoCalc";
    color: #d1a7ff;
    position: absolute;
    top: 5px;
    left: 0px;
    z-index: -2;
    transition: 0.2s;

}
.navBar-cont-user:hover::after, .navBar-cont-user:hover::before{
    top:0px;
}

a.router-link-active{
    position: relative;
    z-index: 1;
}
a.router-link-active div{
    color: #8958BE !important;
}
a.router-link-active img{
    filter: brightness(0) saturate(100%) invert(36%) sepia(100%) saturate(400%) hue-rotate(230deg) brightness(100%) contrast(100%) ;

}
a.router-link-active:hover::after{
    transform: translateY(3px);
    background-color: #dec0ff;
    filter: drop-shadow(0 0px 5px #d5aaff);
}
a.router-link-active:hover::before{
    background-color: #d5aaff;
    filter: drop-shadow(0 0px 5px #d5aaff);
}
a.router-link-active::before {
    transition: 0.3s;
    z-index: -1 ;
    content: "";
    position: absolute;
    height: 80%;
    width: 110%; 
    background-color: #ddbcff;
    border-radius: 0 30px 30px 0;
    top: calc0;
    left: 0;
    pointer-events: none; 
}

a.router-link-active::after {
    transition: 0.3s;
    z-index: -2 ;
    content: "";
    position: absolute;
    height: 80%;
    width: 110%; 
    background-color: #e7d1ff;
    border-radius: 0 30px 30px 0;
    top: 13px;
    left: 0;
    pointer-events: none; 
}
.navBar-cont-routes a:not(.router-link-active)::before {
    transform: translateX(-200px);
    transition: 0.3s;
    z-index: -2 ;
    content: "";
    position: absolute;
    height: 80%;
    width: 110%; 
    background-color: #ffa4d7;
    border-radius: 0 30px 30px 0;
    top: 13px;
    left: 0;
    pointer-events: none; 
}
.navBar-cont-routes a:not(.router-link-active)::after{
    transform: translateX(-200px);
    transition: 0.3s;
    z-index: -1 ;
    content: "";
    position: absolute;
    height: 80%;
    width: 110%; 
    background-color: #ff95d1;
    border-radius: 0 30px 30px 0;
    top: 0;
    left: 0;
    pointer-events: none; 
}
.navBar-cont-routes a:not(.router-link-active){
    transition: 0.3s;
    position: relative;
    z-index: 1;
}
.navBar-cont-routes a:not(.router-link-active):hover::after, .navBar-cont-routes a:not(.router-link-active):hover::before{
    transform: translateX(0px);
}
.navBar-cont-routes a:not(.router-link-active):hover div{
    color: #b7568d;
}
.navBar-cont-routes a:not(.router-link-active) img{
    transition: 0.1s;
}
.navBar-cont-routes a:not(.router-link-active):hover img{
    filter: brightness(0) saturate(100%) invert(36%) sepia(100%) saturate(400%) hue-rotate(270deg) brightness(100%) contrast(100%) ;
}
.navBar-cont-user{
    font-weight: 500;
    display: flex;
    align-items: center;
    align-self: flex-start;
    margin-bottom: 40px;
    position: relative;
    z-index: 3;
}
.navBar-cont-routes{
    align-self: flex-start;
    width: 60%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 80%;
    align-items: flex-start;
}
.icon{
    object-fit: cover;
    width: 25px;
    height: 25px;
    margin-right: 3px;
}
.text{
    font-family: "Nunito", sans-serif;
    font-optical-sizing: auto;
    font-style: normal;
    padding-left: 30px;
    font-weight: 700;
    height: 4rem;
    width: 100%;
    font-size: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    color: #848484;
}
a{
    text-decoration: none;
}
h2{
  /* font-family: "Inter", sans-serif; */
  font-family: "Nunito", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
  font-weight: 600;
  font-size: 1.8rem;
  margin-left: 5px;
  color: #222;
}
.navBar-cont{
    justify-content: flex-start;
    align-items: center;
    display: flex;
    flex-direction: column;
    background-color: #F3F3F3;
    width: 15vw;
    box-shadow: 0 0 4px 0 rgba(1, 1, 1, 0.25);
}
</style>
