<template>
  <header>
    <nav class="bg-transparent px-4 lg:px-6 py-2.5">
      <div class="flex flex-wrap justify-between items-center content-center
      text-lg md:text-4xl lg:text-5xl h-12 md:h-24 lg:h-32 md:mx-4 lg:mx-8">
        <span class="self-center font-bold whitespace-nowrap">CHendLess</span>
        <div class="flex items-center lg:order-2 space-x-2.5 md:space-x-5 lg:space-x-7">
            <PurpleYellowButton v-if="purpleYellow">
              Sign in
            </PurpleYellowButton>
            <PurpleBlueButton v-if="!purpleYellow">
              Sign in
            </PurpleBlueButton>
          <button data-collapse-toggle="mobile-menu-2" type="button" class="" aria-controls="mobile-menu-2" aria-expanded="false">
            <span class="sr-only">Open main menu</span>
            <svg class="w-8 h-8 md:w-20 md:h-16 lg:w-24 lg:h-20" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
            <svg class="hidden w-8 h-8 md:w-20 md:h-16 lg:w-24 lg:h-20" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
          </button>
        </div>

      </div>
    </nav>
  </header>
</template>

<script>
import PurpleBlueButton from "./purplebluebutton.vue";
import PurpleYellowButton from "./purpleYellowButton.vue";

export default {
  name: 'CustomHeadBar',
  components: {PurpleYellowButton, PurpleBlueButton},
  props: {
    purpleYellow: {
      type: Boolean,
      required: true,
    },
  }
};
</script>