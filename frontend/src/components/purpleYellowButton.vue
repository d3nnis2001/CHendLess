<template>
  <button :class="buttonClasses" type="button">
    <slot>Default Text</slot>
  </button>
</template>

<script>
export default {
  name: 'PurpleYellowButton',
  props: {
    gradientVersion: {
      type: Number,
      required: false,
      default: 2
    },
  },
  computed: {
    buttonClasses() {
      return [
        'gradientbutton',
        `gradientbutton${this.gradientVersion}`,
        'relative',
        'text-white',
        'focus:ring-4',
        'focus:outline-none',
        'focus:ring-blue-300',
        'dark:focus:ring-blue-800',
        'font-medium',
        'text-sm',
        'px-7',
        'md:px-14',
        'lg:px-20',
        'py-2.5',
        'text-center',
        'rounded-full',
        'h-fit',
        'w-fit',
        'md:text-3xl'
      ];
    }
  }
};
</script>

<style>
.gradientbutton {
  cursor: pointer;
  /* Define common gradient styles */
}

.gradientbutton1 {
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

.gradientbutton2 {
  background-image: linear-gradient(
      100deg,
      #d036fc,
      #fdca51,
      #fdca51,
      #d036fc);
  background-size: 300%;
  background-position: left;
  transition: background-position 1s;
}

.gradientbutton:hover {
  background-position: right;
}
</style>