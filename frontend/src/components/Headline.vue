<template>
  <p :class="computedClasses">
    <slot>Default Text</slot>
  </p>
</template>

<script>
export default {
  name: 'Headline',
  props: {
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
  },
  computed: {
    computedClasses() {
      return [
        'styled-text',
        `${this.sizeDefault}`,
        'text-left',
        'font-bold',
        `md:${this.sizeMD}`,
        `lg:${this.sizeLG}`,
        'text-shadow-md',
        'shadow-black-dark'
      ];
    }
  }
};
</script>

<style>
.styled-text {
  line-height: 1.15;
}
</style>