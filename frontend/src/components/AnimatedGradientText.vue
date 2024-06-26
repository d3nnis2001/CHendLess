<template>
    <div class="relative">
      <Headline v-if="glow" class="absolute blur-sm text-transparent text-shadow-none bg-gradient-to-r bg-clip-text gradient-text animate-gradient">
        <slot>Default Text</slot>
      </Headline> 
      <Headline class="relative text-transparent text-shadow-none bg-gradient-to-r bg-clip-text gradient-text animate-gradient">
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
    }
  };
  </script>