<template>
    <div class="content-cont">
        <div class="content-cont-calc">
            <div class="content-cont-calc-var">
                <h2>INPUT DATA</h2>
                <form>
                    <div>a = <input/></div>
                    <div>b = <input/></div>
                </form>
            </div>
            <div class="content-cont-calc-result">
                <div>
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Temporibus totam, veritatis perspiciatis molestias beatae asperiores dignissimos. Ipsa exercitationem illo, accusamus eius, voluptatibus ut, iste minus architecto explicabo aliquid soluta commodi!
                </div>
                <button>SOLVE</button>
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

</script>
<style scoped>
    h2, h1, h3{
    font-weight: 400;
    }
    .content-cont-calc-var{
        display: flex;
        flex-direction: column;
        width: 40%;
        height: 90%;
        border: 2px solid red;
    }
    .content-cont-calc-var form{
        display: flex;
        flex-direction: column;
    }
    .content-cont-calc-result{
        justify-content: space-evenly;
        align-items: center;
        flex-direction: column;
        display: flex;
        height: 90%;
        width: 50%;
        border: 2px solid green;
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
    .content-cont-calc-result button{
        font-size: 1.2rem;
        color: white;
        align-self: flex-end;
        margin-right: 5%;
        width: 30%;
        height: 10%;
        background: linear-gradient(90deg, rgba(204,155,255,1) 0%, rgba(214,177,253,1) 100%);
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