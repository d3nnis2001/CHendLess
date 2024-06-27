<template>
  <div class="hero flex flex-col h-screen bg-no-repeat bg-cover bg-center absolute rounded-b-3xl">
    <CustomHeadBar :gradientVersion=1></CustomHeadBar>
    <div class="flex-container">
      <div class="content">
        <Headline>Never buy <br> </Headline>
        <Headline><AnimatedGradientText class="my-1.5" :glow=true>overpriced</AnimatedGradientText></Headline>
        <Headline>again.</Headline>
        <PurpleYellowButton class="mt-10" @click="navigateToUpload" :gradientVersion=1>
          Start now
        </PurpleYellowButton>
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

  <div class="hero-footer content-center rounded-t-3xl">
    <GetStartedNow></GetStartedNow>
  </div>

  <footer class="w-full h-20 md:h-40 lg:h-48 rounded-t-3xl text-center">
    <div class="grid grid-cols-[1fr_3fr] gap-2 md:gap-4 h-full items-center justify-items-center">
        <!-- 25% Column -->
        <div>
            <span class="self-center font-bold whitespace-nowrap text-sm sm:text-lg md:text-3xl lg:text-4xl xl:text-5xl 2xl:text-6xl">CHendLess</span>
        </div>
        <!-- 75% Column -->
        <div class="grid grid-cols-2 grid-rows-2 md:flex w-full h-full items-center justify-around font-medium text-ssm sm:text-base md:text-lg lg:text-2xl xl:text-3xl 2xl:text-4xl">
            <div>
                <a href="https://www.tiktok.com/explore" target="_blank" rel="noopener noreferrer">
                    <span>TikTok</span>
                </a>
            </div>
            <div>
                <a href="https://www.instagram.com" target="_blank" rel="noopener noreferrer">
                    <span>Instagram</span>
                </a>
            </div>
            <div>
                <RouterLink to="/datenschutz">
                    <span>Datenschutzerklärung</span>
                </RouterLink>
            </div>
            <div>
                <RouterLink to="/impressum">
                    <span>Impressum</span>
                </RouterLink>
            </div>
        </div>
    </div>
</footer>

</template>

<script>
import CustomHeadBar from "../components/headbar.vue";
import StepComponent from "../components/StepComponent.vue";
import Headline from "../components/Headline.vue";
import AnimatedGradientText from "../components/AnimatedGradientText.vue";
import PurpleYellowButton from "../components/purpleYellowButton.vue";
import GetStartedNow from "../components/GetStartedNow.vue";
import { RouterLink } from "vue-router";

export default {
  name: 'Start',
  components: {PurpleYellowButton, CustomHeadBar, StepComponent, Headline, AnimatedGradientText, GetStartedNow},
  methods: {
    navigateToUpload() {
      this.$router.push('/upload');
    }
  }
}


</script>

<style scoped>

.hero {
  background: url('../assets/banner.svg') no-repeat center center;
  background-size: cover;
  height: 100vh;
  width: 100vh;
  position: relative;
  min-width: 100%;
  max-width:100%;
}

.hero-footer {
  background: url('../assets/bannerfooter.svg') no-repeat center center;
  background-size: cover;
  height: 75vh;
  position: relative;
  min-width: 100%;
  max-width:100%;
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

/* * { 
  border: 1px solid red; 
} */

.highlight {
  color: #f39c12;
}

.q-btn {
  margin-top: 1rem;
}
</style>
