<template>
  <div>
    <label class="relative cursor-pointer">
      <!-- Hidden file input -->
      <input type="file" ref="fileInput" class="hidden" @change="handleFileChange" accept="image/png, image/gif, image/jpeg">
      <!-- Styled button-like appearance -->
      <div class="px-6 py-2 text-black-dark bg-white-dark font-bold rounded-full shadow-lg shadow-zinc-800 hover:bg-gray-200 transition-colors duration-300 ease-in-out">
        Browse files
      </div>
    </label>
  </div>
</template>

<script>
export default {
  name: 'BrowseButton',
  methods: {
    handleFileChange(event) {
      const selectedFile = event.target.files[0];
      this.$emit('file-selected', selectedFile);
      this.resetFileInput();
    },
    resetFileInput() {
      this.$refs.fileInput.value = '';
    }
  }
};
</script>

<style scoped>
/* Optional: Style the label to match the button appearance */
label {
  display: inline-block;
}
</style>
