<script setup>

</script>

<template>
    <div class="navBar-cont">
        <h2 class="navBar-cont-user"> <img src="../assets/Generic avatar.svg">Nick</h2>
        <div class="navBar-cont-routes">
            <h2>CALCULATION</h2>
            <div class="text"> <img class="icon" src="../assets/Box.svg">Nok</div>
            <div class="text selected"> <img class="icon" src="../assets/Octagon.svg">Nod</div>
            <div class="text"> <img class="icon" src="../assets/Cpu.svg">Abs</div>
            <h2>RESULTS</h2>
            <div class="text"> <img class="icon" src="../assets/Rotate ccw.svg">Recent</div>
        </div>
    </div>
</template>

<style scoped>
.navBar-cont-routes h2{
    margin-left: 10px;
}
.selected{
    color: #8958BE !important;
    position: relative;
    z-index: 1;
}
.selected::before {
    z-index: -1 ;
    content: "";
    position: absolute;
    height: 80%;
    width: 100%; 
    background-color: #ddbcff;
    border-radius: 0 30px 30px 0;
    top: calc(0 - 20%);
    left: 0;
    pointer-events: none; 
}
.selected::after {
    z-index: -2 ;
    content: "";
    position: absolute;
    height: 80%;
    width: 100%; 
    background-color: #e7d1ff;
    border-radius: 0 30px 30px 0;
    top: 13px;
    left: 0;
    pointer-events: none; 
}
.navBar-cont-user{
    display: flex;
    align-items: center;
    align-self: flex-start;
    margin-left: 25px;
}
.navBar-cont-routes{
    align-self: flex-start;
    width: 85%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    height: 50%;
    align-items: flex-start;
}
.icon{
    object-fit: cover;
    width: 25px;
    height: 25px;
}
.text{
    padding-left: 25px;
    height: 4rem;
    width: 100%;
    font-size: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    color: #848484;
}
h2{
  font-weight: 500;
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
