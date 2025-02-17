<template>
  <CustomHeadBar :profileInsteadOfButton="true"></CustomHeadBar>
  <div class="flex flex-col items-start extraMar">
    <p class="font-bold">Scanned Item:</p>
    <div class="flex flex-row justify-center items-center">
      <div class="w-48 h-48 reck flex items-center justify-center rounded-lg mr-5">
        <img src='../../src/assets/productImage.png' alt="Product" class="w-40 h-40">
      </div>
      <div class="w-96 h-48 reck items-center justify-center flex rounded-lg">
        <p class="font-bold">Original Price: 50,00€</p>
      </div>
    </div>
  </div>
  <div class="flex flex-col justify-center items-start extraMar">
    <p class="font-bold">We have found 13 similar items:</p>
    <div class="flex flex-row items-center">
      <div class="h-30 reck headlineBar flex flex-row items-center justify-around">
        <p class="font-bold" v-for="(item, index) in items" :key="index">{{ item }}</p>
      </div>
    </div>
  </div>
  <div class="w-full flex flex-col items-center">
    <ProductListItem
        v-for="(product, index) in productList"
        :key="index"
        :link="product[0]"
        :shop="product[1]"
        :saved-money-pro="product[2]"
        :saved-money="product[3]"
        :price="product[4]"
        :name="product[5]"
        :picture="product[6]"
        :color="index % 2 === 0"
    ></ProductListItem>
  </div>
</template>

<script>
import ProfileButton from "../components/ProfileButton.vue";
import Headline from "../components/Headline.vue";
import CustomHeadBar from "../components/headbar.vue";
import ProductListItem from "../components/ProductListItem.vue";

export default {
  name: 'Result',
  components: { ProductListItem, CustomHeadBar, Headline, ProfileButton },
  data() {
    return {
      items: ["Picture", "Name", "Price", "Saved Money (€)", "Saved Money (%)", "Shop", "Link"],
      productList: [
        ["https://de.aliexpress.com/", "Aliexpress", "25%", "25€", "100€", "Item 1", "../../src/assets/productImage.png"],
        ["https://de.aliexpress.com/", "Aliexpress", "25%", "25€", "100€", "Item 2", "../../src/assets/productImage.png"],
        ["https://de.aliexpress.com/", "Aliexpress", "25%", "25€", "100€", "Item 3", "../../src/assets/productImage.png"],
        ["https://de.aliexpress.com/", "Aliexpress", "25%", "25€", "100€", "Item 4", "../../src/assets/productImage.png"]
      ]
    };
  }
}
</script>

<style scoped>

.extraMar {
  margin-left: 7.5vw;
}

.reck {
  border: 2px solid;
  border-color: rgba(255, 255, 255, 0.2);
  border-image-slice: 1;
  box-sizing: border-box;
  background: linear-gradient(
      to right,
      rgba(255, 255, 255, 0.15) 0%,
      rgba(255, 255, 255, 0.10) 100%
  );
  border-radius: 0.5rem;
}

.headlineBar {
  width: 85vw;
  height: 39px;
}

</style>
