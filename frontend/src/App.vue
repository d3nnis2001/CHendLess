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
    <StepComponent 
      :imageLeft=false 
      :step=1
      title="Upload a picture" 
      description="Simply upload a picture or paste a <br> link of the product you want to find" 
      image="/src/assets/laptop.svg" 
      altText="laptop"/>

    <StepComponent 
      :imageLeft=true 
      :step=2 
      title="Insert a price" 
      description="Put in the price you would've originally <br> paid for the queried product" 
      image="/src/assets/part2instr.png" 
      altText="numbers"/>

    <StepComponent 
      :imageLeft=false 
      :step=3
      title="Get the results" 
      description="After checking the web for <br> correlating products, we get you <br> a list of all shops that offer the product" 
      image="/src/assets/results.png" 
      altText="results"/>
  </div>

</template>

<script>
import CustomHeadBar from "./components/headbar.vue";
import PurpleBlueButton from "./components/purplebluebutton.vue";
import StepComponent from "./components/StepComponent.vue";

export default {
  name: 'IndexPage',
  components: {PurpleBlueButton, CustomHeadBar, StepComponent}
}
</script>

<style scoped>
.hero {
  background: url('../../frontend/src/assets/banner.svg') no-repeat center center;
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
