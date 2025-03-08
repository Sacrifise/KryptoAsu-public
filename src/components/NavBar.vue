<script setup>

</script>

<template>
    <div class="navBar-cont">
        <h2 class="navBar-cont-user"> <img src="../assets/Generic avatar.svg">Nick</h2>
        <div class="navBar-cont-routes">
            <h2>CALCULATION</h2>
            <div class="text unselected"> <img class="icon" src="../assets/Box.svg">Nok</div>
            <div class="text selected"> <img class="icon" src="../assets/Octagon.svg">Nod</div>
            <div class="text unselected"> <img class="icon" src="../assets/Cpu.svg">Abs</div>
            <h2>RESULTS</h2>
            <div class="text unselected"> <img class="icon" src="../assets/Rotate ccw.svg">Recent</div>
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
.selected:hover::after{
    transform: translateY(3px);
    background-color: #dec0ff;
    filter: drop-shadow(0 0px 5px #d5aaff);
}
.selected:hover::before{
    background-color: #d5aaff;
    filter: drop-shadow(0 0px 5px #d5aaff);
}
.selected::before {
    transition: 0.3s;
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
    transition: 0.3s;
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
.unselected::before {
    transform: translateX(-200px);
    transition: 0.3s;
    z-index: -2 ;
    content: "";
    position: absolute;
    height: 80%;
    width: 100%; 
    background-color: #ffa4d7;
    border-radius: 0 30px 30px 0;
    top: 13px;
    left: 0;
    pointer-events: none; 
}
.unselected::after{
    transform: translateX(-200px);
    transition: 0.3s;
    z-index: -1 ;
    content: "";
    position: absolute;
    height: 80%;
    width: 100%; 
    background-color: #ff95d1;
    border-radius: 0 30px 30px 0;
    top: calc(0 - 20%);
    left: 0;
    pointer-events: none; 
}
.unselected{
    transition: 0.3s;
    position: relative;
    z-index: 1;
}
.unselected:hover::after, .unselected:hover::before{
    transform: translateX(-10px);
}
.unselected:hover{
    color: #b7568d;
}
.unselected img{
    transition: 0.1s;
}
.unselected:hover img{
    filter: brightness(0) saturate(100%) invert(36%) sepia(100%) saturate(400%) hue-rotate(270deg) brightness(100%) contrast(100%) ;
}
.navBar-cont-user{
    display: flex;
    align-items: center;
    align-self: flex-start;
    margin-left: 25px;
}
.navBar-cont-routes{
    align-self: flex-start;
    width: 60%;
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
