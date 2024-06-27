<template>
    <div :class="['items-center grid grid-rows-3 box-border justify-items-center lg:justify-around p-5 py-10 sm:p-10 lg:p-16 xl:p-20 xl:py-24 border-2 text-center m-7 md:m-10 lg:m-20 rounded-3xl border-gray-400 h-72 md:h-80 lg:h-96 xl:h-100 2xl:h-125 bg-white-dark bg-opacity-20 backdrop-blur-2xl shadow-2xl shadow-zinc-900',
        { 'getstartednow': isVisible }
    ]"
    :style="{ opacity: isVisible ? 1 : 0 }"
    ref="getstartednow"
    >
      <span class="text-shadow-none font-semibold text-2xl sm:text-4xl md:text-7xl xl:text-8xl 2xl:text-10xl">
        Get started now!
      </span>
      <span class="leading-tight text-lg sm:text-xl md:text-2xl lg:text-4xl 2xl:text-5xl">
        Register now and get <AnimatedGradientText :glow=true>1 weekly</AnimatedGradientText> scan for free!
      </span>
      <PurpleYellowButton class="xl:h-16 xl:text-4xl">
        Start now
      </PurpleYellowButton>
    </div>
  </template>
  
    <script>
    import AnimatedGradientText from "../components/AnimatedGradientText.vue";
    import PurpleYellowButton from "../components/purpleYellowButton.vue";

    export default {
      name: 'GetStartedNow',
      components: {PurpleYellowButton, AnimatedGradientText},
      data() {
        return {
          isVisible: false
        };
      },
      mounted() {
        window.addEventListener('scroll', this.handleScroll);
        this.handleScroll(); // Check initial scroll position
      },
      destroyed() {
        window.removeEventListener('scroll', this.handleScroll);
      },
      methods: {
        handleScroll() {
          const componentTop = this.$refs.getstartednow.getBoundingClientRect().top;
          const viewportHeight = window.innerHeight;
          const offset = viewportHeight * 0.25;
          
          // Trigger when the entire component is in the viewport
          if (componentTop < viewportHeight-offset && componentTop > -this.$refs.getstartednow.clientHeight) {
            this.isVisible = true;
            window.removeEventListener('scroll', this.handleScroll); // Optional: Remove listener once visible
          }
        }
      }
    };
    </script>
    
    <style>
    @keyframes bounceIn {
      0% {
        opacity: 0;
        transform: translateY(-50px);
      }
      50% {
        opacity: 0.5;
        transform: translateY(10px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }
    
    .getstartednow {
      animation: bounceIn 1s ease-out; /* Adjust animation duration and easing as needed */
    }
    </style>