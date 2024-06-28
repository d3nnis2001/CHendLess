<template>
  <div :class="['h-30', 'reckt', 'productBar', { 'reckt-colored': color }, 'flex', 'flex-row', 'items-center', 'justify-around']">
    <img :src="picture" alt="Product Image" class="w-16 h-16">
    <p>{{ name }}</p>
    <p>{{ price }}</p>
    <p style="color: #24ff00">{{ savedMoney }}</p>
    <p style="color: #24ff00">{{ savedMoneyPro }}</p>
    <p>{{ shop }}</p>
    <a :href="link" target="_blank">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M3.25 23.25C2.5625 23.25 1.97396 23.0052 1.48438 22.5156C0.994792 22.026 0.75 21.4375 0.75 20.75V3.25C0.75 2.5625 0.994792 1.97396 1.48438 1.48438C1.97396 0.994792 2.5625 0.75 3.25 0.75H12V3.25H3.25V20.75H20.75V12H23.25V20.75C23.25 21.4375 23.0052 22.026 22.5156 22.5156C22.026 23.0052 21.4375 23.25 20.75 23.25H3.25ZM9.125 16.625L7.375 14.875L19 3.25H14.5V0.75H23.25V9.5H20.75V5L9.125 16.625Z" fill="white"/>
      </svg>

    </a>

  </div>
</template>

<script>
export default {
  name: 'ProductListItem',
  props: {
    picture: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    price: {
      type: String,
      required: true
    },
    savedMoney: {
      type: String,
      required: true
    },
    savedMoneyPro: {
      type: String,
      required: true
    },
    shop: {
      type: String,
      required: true
    },
    link: {
      type: String,
      required: true
    },
    color: {
      type: Boolean,
      required: false,
      default: false
    }
  }
}
</script>

<style scoped>
.reckt {
  border-image-slice: 1;
  box-sizing: border-box;
  background: linear-gradient(
      to right,
      rgba(255, 255, 255, 0.05) 0%,
      rgba(255, 255, 255, 0.02) 100%
  );
  border-radius: 0.5rem;
}

.reckt-colored {
  background: #1b1b1b;
}

.productBar {
  width: 85vw;
  height: 12vh;
}
</style>
