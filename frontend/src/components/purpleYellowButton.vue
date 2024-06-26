<template>
  <button type="button"
          class="gradientbutton2 relative text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800
          font-medium text-sm px-7 md:px-14 lg:px-20 py-2.5 text-center rounded-full
          h-fit w-fit md:text-3xl">
    <slot>Default Text</slot>
  </button>
</template>

<script>
export default {
  name: 'PurpleYellowButton'
};
</script>

<style>
/* Change the position of the whole background to give it the appearance of an animation*/
.gradientbutton2 {
  cursor: pointer;
  background-image: linear-gradient(
      100deg,
      #d036fc,
      #fdca51,
      #fdca51,
      #d036fc);
  background-size: 300%;
  background-position: left;
  transition: background-position 1s;
  text-align: center;
}

.gradientbutton2:hover {
  background-position: right;
}
</style>