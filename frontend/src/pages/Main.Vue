<template>
  <div id="app">
    <div class="spacing">
      <h1>Image Upload or Link</h1>
      <h3>Upload the image of the product or insert a link</h3>
      <h5>The following link types are supported: JPG, PNG, WEBP, SVG</h5>
    </div>
    <div class="spacing">
      <input type="file" @change="onFileChange"/>
      <input v-model="imageUrl" placeholder="Enter image URL" />
    </div>
    <div class="">
      <q-btn style="width: 200px" color="primary" size="lg" label="Search Product" @click="uploadFile" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Notify } from 'quasar';
import {sendImage} from "@/api/main";

export default {
  data() {
    return {
      selectedFile: null,
      imageUrl: '',
      images: []
    };
  },
  methods: {
    onFileChange(event) {
      this.selectedFile = event.target.files[0];
    },
    async uploadFile() {
      if (!this.selectedFile && !this.imageUrl) {
        Notify.create({
          message: 'Please upload a file or enter a URL',
          color: 'negative',
          position: 'top'
        });
        return;
      }

      if (this.selectedFile) {
        if (!this.isValidImage(this.selectedFile)) {
          Notify.create({
            message: 'Invalid file type. Only JPG, PNG, and GIF are allowed.',
            color: 'negative',
            position: 'top'
          });
          return;
        }

        const formData = new FormData();
        formData.append('file', this.selectedFile);
        const response = await sendImage(formData)
      }
    },
    isValidImage(file) {
      const validTypes = ['image/jpeg', 'image/png', 'image/webp', 'image/svg'];
      return validTypes.includes(file.type);
    }
  }
};
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  text-align: center;
  align-items: center;
  justify-content: center;
  color: #2c3e50;
}
h1, h3, h5 {
  margin-bottom: 50px;
  padding: 0;
}
</style>