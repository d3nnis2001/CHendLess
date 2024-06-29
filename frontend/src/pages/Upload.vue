<template>
  <div class="min-h-screen flex flex-col" @paste="handlePaste">
    <CustomHeadBar :gradientVersion="2"></CustomHeadBar>
    <div class="flex-grow hero-footer content-center flex flex-col justify-center items-center">
      <div class="items-center flex flex-col lg:flex-row box-border justify-items-center lg:justify-center p-5 sm:p-10 md:p-16 border-2
      m-7 md:m-10 rounded-3xl border-gray-400 h-auto lg:h-96
      bg-white-dark bg-opacity-15 shadow-2xl shadow-zinc-900">
        <div 
          class="bordermoving flex flex-col justify-center items-center p-10 md:m-4 rounded-3xl"
          @dragover.prevent
          @dragenter.prevent
          @drop.prevent="handleDrop"
        >
          <img src='../../src/assets/upload.png' alt="Upload" class="w-16 h-16 mb-4">
          <p class="text-2xl text-center mb-4">
            <strong>Drag and Drop to upload</strong> <br> or
          </p>
          <BrowseButton @file-selected="handleFile"></BrowseButton>
          <!-- Display selected file name if available -->
          <p v-if="uploadedFileName" class="mt-2 text-center">{{ uploadedFileName }}</p>
        </div>
        <div class="flex flex-col text-center ml-0 lg:ml-10 mt-10 lg:mt-0">
          <p class="font-bold text-2xl md:text-5xl mb-5">
            Upload your image
          </p>
          <p class="text-xl md:text-4xl">
            JPG, GIF or PNG formats that <br> are max. 2000 x 2000 or 16MB. <br>
            If your image size is bigger,<br> please compress it.
          </p>
        </div>
      </div>
    </div>
  </div>
  <Impressum/>
</template>

<script>
import CustomHeadBar from "../components/headbar.vue";
import BrowseButton from "../components/BrowseButton.vue";
import Impressum from "../components/Impressum.vue";

export default {
  name: 'Upload',
  components: {
    BrowseButton,
    CustomHeadBar,
    Impressum
  },
  data() {
    return {
      uploadedFile: null,
      uploadedFileName: ''
    };
  },
  methods: {
    handleDrop(event) {
      const files = event.dataTransfer.files;
      if (files.length > 0) {
        this.uploadFile(files[0]);
      }
    },
    handleFile(file) {
      this.uploadFile(file);
    },
    handlePaste(event) {
      console.log("Paste event detected");
      const items = event.clipboardData.items;
      console.log("Clipboard items:", items);
      for (let i = 0; i < items.length; i++) {
        if (items[i].kind === 'file' && items[i].type.startsWith('image/')) {
          const file = items[i].getAsFile();
          console.log("Image file detected:", file);
          this.uploadFile(file);
          break;
        }
      }
    },
    uploadFile(file) {
      if (this.validateFile(file)) {
        this.uploadedFile = file;
        this.uploadedFileName = file.name;
        // Handle the file upload logic here
        console.log('File uploaded:', file.name);
      } else {
        this.uploadedFileName = '';
        console.error('Invalid file');
      }
    },
    validateFile(file) {
      const validTypes = ['image/jpeg', 'image/png', 'image/gif'];
      const maxSize = 16 * 1024 * 1024; // 16MB in bytes
      return validTypes.includes(file.type) && file.size <= maxSize;
    }
  }
};
</script>

<style scoped>
.bordermoving {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 280px;
  width: 300px;
  background: linear-gradient(90deg, white 50%, transparent 50%),
  linear-gradient(90deg, white 50%, transparent 50%),
  linear-gradient(0deg, white 50%, transparent 50%),
  linear-gradient(0deg, white 50%, transparent 50%);
  background-repeat: repeat-x, repeat-x, repeat-y, repeat-y;
  background-size: 1em 0.25em, 1em 0.25em, 0.25em 1em, 0.25em 1em;
  background-position: 0 0, 100% 100%, 0 100%, 100% 0;
  padding: 20px;
  border-radius: 1em;
  position: relative;
  animation: border-dance 12s infinite linear;
  overflow: hidden;
}

.bordermoving::before {
  content: "";
  position: absolute;
  top: -4px; left: -4px; right: -4px; bottom: -4px;
  border-radius: inherit;
  border: 4px dashed transparent;
  background: inherit;
  background-clip: border-box;
  background-origin: border-box;
  z-index: -1;
}

@keyframes border-dance {
  0% {
    background-position: 0 0, 100% 100%, 0 100%, 100% 0;
  }
  100% {
    background-position: 100% 0, 0 100%, 0 0, 100% 100%;
  }
}
</style>
