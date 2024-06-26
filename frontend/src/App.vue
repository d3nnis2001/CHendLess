

<template>
  <div class="hero flex flex-col h-screen bg-no-repeat bg-cover bg-center absolute w-fit rounded-b-3xl">
    <CustomHeadBar></CustomHeadBar>
    <div class="flex-container">
      <div class="content">
        <Headline>Never buy <br> </Headline>
        <AnimatedGradientText :glow=true class="my-1.5">overpriced</AnimatedGradientText>
        <Headline>again.</Headline>
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
      description="Simply upload a picture or paste a link of the product you want to find" 
      image="/src/assets/laptop2.png" 
      altText="laptop"/>

    <StepComponent 
      :imageLeft=true 
      :step=2 
      title="Insert a price" 
      description="Put in the price you would've originally paid for the queried product" 
      image="/src/assets/part2instr.png" 
      altText="numbers"/>

    <StepComponent 
      :imageLeft=false 
      :step=3
      title="Get the results" 
      description="After checking the web for correlating products, we get you a list of all shops that offer the product" 
      image="/src/assets/results.png" 
      altText="results"/>
  </div>

</template>

<script>
import CustomHeadBar from "./components/headbar.vue";
import PurpleBlueButton from "./components/purplebluebutton.vue";
import StepComponent from "./components/StepComponent.vue";
import Headline from "./components/Headline.vue";
import AnimatedGradientText from "./components/AnimatedGradientText.vue";

export default {
  name: 'IndexPage',
  components: {PurpleBlueButton, CustomHeadBar, StepComponent, Headline, AnimatedGradientText}
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
