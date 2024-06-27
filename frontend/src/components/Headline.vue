<template>
  <p class="styled-text text-left font-bold text-4xl sm:text-6xl md:text-7xl lg:text-8xl xl:text-9xl 2xl:text-10xl text-shadow-md shadow-black-dark">
    <slot>Default Text</slot>
  </p>
</template>

<script>
export default {
  name: 'Headline'
};
</script>

<style scoped>
.styled-text {
  line-height: 1.15;
}
</style>
