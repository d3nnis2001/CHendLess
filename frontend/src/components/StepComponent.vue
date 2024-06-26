<template>
    <div 
      :class="[
        'flex items-center flex-row box-border justify-around p-10 border-2 m-7 md:m-10 lg:m-20 rounded-2xl border-gray-400'
      ]" 
      :style="{ backgroundColor: '#323232'}"
    >
      <div v-if="imageLeft">
        <img :src="image" :alt="altText" class="image-steps-hover">
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
        <img :src="image" :alt="altText" class="image-steps-hover">
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
    }
  }
  </script>

<style>
    .image-steps-hover {
    transition: ease-in-out;
    transition-duration: 650ms;
    }

    .image-steps-hover:hover {
    scale: 120%;
    }
</style>