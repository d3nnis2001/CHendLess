<template>
    <p class="styled-text text-5xl text-left font-bold md:text-8xl lg:text-10xl text-shadow-md shadow-black-dark">
      <slot>Default Text</slot>
    </p>
  </template>
  
  <script>
  export default {
    name: 'Headline'
  };
  </script>
  
  <style>
    .styled-text {
        line-height: 1.15;
    }
  </style>