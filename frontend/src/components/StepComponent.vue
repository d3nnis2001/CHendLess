<template>
  <div
    :class="[
      'flex items-center flex-row box-border justify-between lg:justify-around p-10 border-2 my-7 md:my-10 lg:my-20 mx-7 md:mx-10 lg:mx-20 xl:mx-32 2xl:mx-40 rounded-3xl border-gray-400 h-72 md:h-80 lg:h-96',
      { 'step-component': isVisible }
    ]"
    :style="{ backgroundColor: '#323232', opacity: isVisible ? 1 : 0 }"
    ref="stepComponent"
  >
    <div v-if="imageLeft">
      <img :src="image" :alt="altText" class="image-steps-hover shadow-2xl hover:shadow-zinc-900">
    </div>
    <div :class="[imageLeft ? 'text-right' : 'text-left']">
      <p :class="textClass">
        <strong>
          Step {{ step }}:<br>{{ title }}
        </strong>
      </p>
      <p class="mt-10" v-html="description"></p>
    </div>
    <div v-if="!imageLeft">
      <img :src="image" :alt="altText" class="image-steps-hover shadow-2xl hover:shadow-zinc-900">
    </div>
  </div>
</template>

  <script>
  export default {
    name: 'StepComponent',
    props: {
      step: {
        type: Number,
        required: true
      },
      imageLeft: {
        type: Boolean,
        default: false
      },
      textClass: {
        type: String,
        default: 'text-2xl md:text-5xl lg:text-7xl'
      },
      title: {
        type: String,
        required: true
      },
      description: {
        type: String,
        required: true
      },
      image: {
        type: String,
        required: true
      },
      altText: {
        type: String,
        default: ''
      }
    },
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
        const componentTop = this.$refs.stepComponent.getBoundingClientRect().top;
        const viewportHeight = window.innerHeight;
        const offset = viewportHeight * 0.15;
        
        // Trigger when the entire component is in the viewport
        if (componentTop < viewportHeight-offset && componentTop > -this.$refs.stepComponent.clientHeight) {
          this.isVisible = true;
          window.removeEventListener('scroll', this.handleScroll); // Optional: Remove listener once visible
        }
      }
    }
  };
  </script>
  
  <style>
  .image-steps-hover {
    transition: ease-in-out;
    transition-duration: 500ms;
  }
  
  .image-steps-hover:hover {
    transform: scale(1.1); /* Adjust the scaling property */
  }
  
  @keyframes bounceIn {
    0% {
      opacity: 0;
      transform: translateY(50px);
    }
    50% {
      opacity: 0.5;
      transform: translateY(-10px);
    }
    100% {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  .step-component {
    animation: bounceIn 1s ease-out; /* Adjust animation duration and easing as needed */
  }
  </style>