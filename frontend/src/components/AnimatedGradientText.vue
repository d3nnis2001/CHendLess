<template>
    <div class="relative inline-block">
      <span v-if="glow" class="absolute blur-sm text-transparent text-shadow-none bg-gradient-to-r bg-clip-text gradient-text animate-gradient">
        <slot>Default Text</slot>
      </span>
      <span class="relative text-transparent text-shadow-none bg-gradient-to-r bg-clip-text gradient-text animate-gradient">
        <slot>Default Text</slot>
      </span>
    </div>
  </template>

  <script>

  export default {
    name: 'AnimatedGradientText',
    props: {
      glow: {
        type: Boolean,
        default: false
      }
    }
  };
  </script>

<style>
  .gradient-text {
    display: inline;
  }
</style>