<template>
  <div class="hero flex flex-col h-screen bg-no-repeat bg-cover bg-center absolute w-screen max-w-screen">
    <CustomHeadBar></CustomHeadBar>
    <div class="flex-container">
      <div class="content">
        <p class="styled-text text-5xl text-left font-bold md:text-8xl lg:text-8xl">Never buy <br> <span class="highlight">overpriced</span> <br> again.</p>
        <PurpleBlueButton class="mt-10">
          Start now
        </PurpleBlueButton>
      </div>
    </div>
  </div>
  <div class="text-l md:text-3xl">
    <div class=" flex items-center flex-row box-border justify-around p-10 border-2 m-7 md:m-10 lg:m-20 rounded-2xl border-gray-400 bg-background_rec" style="background-color: #323232;">
      <div class="">
        <p class="text-2xl md:text-5xl lg:text-7xl">
          <strong> Step 1:<br>Upload a picture </strong>
        </p>
        <p class="mt-10">
          Simply upload a picture or paste a <br> link of the product you want to find
        </p>
      </div>
      <div class="">
        <img src='/src/assets/laptop.svg' alt="Laptop" class="image-steps-hover">
      </div>
    </div>
    <div class="flex items-center text-right flex-row justify-around box-border p-20 border-2 m-7 md:m-10 lg:m-20 rounded-2xl border-gray-400" style="background-color: #323232;">
      <div class="">
        <img src='/src/assets/part2instr.png' alt="numbers" class="image-steps-hover">
      </div>
      <div class="">
        <p class="text-2xl md:text-5xl lg:text-7xl">
          <strong> Step 2:<br>Insert a price </strong>
        </p>
        <p class="mt-10">
          Put in the price you would've originally <br> paid for the queried product
        </p>
      </div>
    </div>
    <div class="box-border flex flex-row justify-around p-20 border-2 m-7 md:m-10 lg:m-20 rounded-2xl border-gray-400" style="background-color: #323232;">
      <div class="">
        <p class="text-5xl">
          <strong> Step 3: Get the results </strong>
        </p>
        <p class="text-2xl">
          After checking the web for
        </p>
        <p class="text-2xl">
          correlating products, we get you
        </p>
        <p class="text-2xl">
          a list of all shops that offer the product
        </p>
      </div>
      <div class="image-container3"></div>
    </div>
  </div>
</template>

<script>
import CustomHeadBar from "./components/headbar.vue";
import PurpleBlueButton from "./components/purplebluebutton.vue";

export default {
  name: 'IndexPage',
  components: {PurpleBlueButton, CustomHeadBar}
}
</script>

<style scoped>
.hero {
  background: url('../../frontend4/src/assets/banner.svg') no-repeat center center;
  background-size: cover;
  height: 100vh;
  position: relative;
  min-width: 100%;
}

.flex-container {
  display: flex;
  justify-content: start;
}

.content {
  padding-left: 10%;
  padding-top: 10vh;
}

.styled-text {
  line-height: 1.15;
}

.image-steps-hover {
  transition: ease-in-out;
  transition-duration: 500ms;
}

.image-steps-hover:hover {
  scale: 110%;
}

.image-container3 {
  background-image: url('../../frontend4/src/assets/results.png');
  width: 50%;
  height: auto;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: right;
}

h1 {
  font-size: 4rem;
  font-weight: bold;
}

.highlight {
  color: #f39c12;
}

.q-btn {
  margin-top: 1rem;
}
</style>
