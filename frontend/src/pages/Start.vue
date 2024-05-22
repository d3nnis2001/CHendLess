<script>

import {useRouter} from "vue-router";

export default {
  setup () {
    const router = useRouter()

    function goToMain() {
      router.push({ path: "/main" })
    }

    return {
      goToMain
    }
  }
}

</script>
<template>
  <div class="hero-section">
    <div class="">
      <div class="absolute-center text-center text-white">
        <h1 class="bg-primary extra_padding">CHendLess</h1>
        <p class="text-primary">Find your favourite products without paying fortune.</p>
        <q-btn color="primary" size="lg" label="Get Started" @click="goToMain" />
      </div>
    </div>
  </div>
</template>

<style>
.extra_padding {
  padding: 25px;
}
</style>