<template>
    <div class="flex items-center text-unselected-default hover:text-white-dark duration-100 ease-in w-full justify-center md:w-fit"> <!-- use w-fit to ensure that you have to hover over the text/svg itself-->
        <svg class="h-10 w-10 flex-none fill-current" :viewBox="viewBox" xmlns="http://www.w3.org/2000/svg">
            <path :d="svgpath"/>
        </svg>

        <span class="ml-2 hidden md:block">
            <slot></slot>
        </span>
    </div>
</template>

<script>
export default {
    name: 'UserTabTextImage',

    props: {
        svgpath: {
            type: String,
            required: true
        },
        viewBox: {
            type: String,
            required: true
        }
    }
};
</script>

<style>
/* * { 
  border: 1px solid red; 
} */
</style>