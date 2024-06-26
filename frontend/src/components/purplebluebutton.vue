<template>
  <button type="button"
          class="gradientbutton relative text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800
          font-medium text-sm px-5 md:px-7 lg:px-10 py-2.5 text-center rounded-full
          h-fit w-fit md:text-3xl">
    <slot>Default Text</slot>
  </button>
</template>

<script>
export default {
  name: 'PurpleBlueButton'
};
</script>

<style>
  /* Change the position of the whole background to give it the appearance of an animation*/
  .gradientbutton {
    cursor: pointer;
    background-image: linear-gradient(
        135deg,
        #ab47bc,
        #ba68c8,
        #ce93d8,
        #ffc107,
        #ffb300,
        #f39c12);
    background-size: 300%;
    background-position: left;
    transition: background-position 0.75s;
    text-align: center;
  }

  .gradientbutton:hover {
    background-position: right;
  }
</style>