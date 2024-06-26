<template>
    <div class="relative inline-block">
      <Headline v-if="glow" class="absolute blur-sm text-transparent text-shadow-none bg-gradient-to-r bg-clip-text gradient-text animate-gradient"
                :size-default="sizeDefault" :size-md="sizeMD" :size-lg="sizeLG">
        <slot>Default Text</slot>
      </Headline>
      <Headline class="relative text-transparent text-shadow-none bg-gradient-to-r bg-clip-text gradient-text animate-gradient"
                :size-default="'sizeDefault'" :size-md="'sizeMD'" :size-lg="'sizeLG'">
        <slot>Default Text</slot>
      </Headline>
    </div>
  </template>

  <script>
  import Headline from "./Headline.vue";

  export default {
    name: 'AnimatedGradientText',
    components: { Headline },
    props: {
      glow: {
        type: Boolean,
        default: false
      },
      sizeDefault: {
        type: String,
        default: "text-5xl",
        required: false
      },
      sizeMD: {
        type: String,
        default: "text-8xl",
        required: false
      },
      sizeLG: {
        type: String,
        default: "text-10xl",
        required: false
      }
    }
  };
  </script>

<style>
  .gradient-text {
    display: inline; /* or inline-block */
    /* Other styles as needed */
  }
</style>