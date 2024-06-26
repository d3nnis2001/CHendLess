<template>
  <div>
    <CustomHeadBar :purpleYellow="true"></CustomHeadBar>
    <div class="hero-footer content-center flex flex-col justify-center items-center rounded-t-3xl mt-20">
      <div class="items-center flex flex-col lg:flex-row box-border justify-items-center lg:justify-center p-16 border-2
      m-7 md:m-10 rounded-3xl border-gray-400 h-auto lg:h-96
      bg-white-dark bg-opacity-15 shadow-2xl shadow-zinc-900">
        <div class="bordermoving flex flex-col justify-center items-center p-10 m-4 rounded-3xl">
          <img src='../../src/assets/upload.png' alt="Upload" class="w-16 h-16 mb-4">
          <p class="text-2xl text-center mb-4">
            <strong>Drag and Drop to upload</strong> <br> or
          </p>
          <BrowseButton></BrowseButton>
        </div>
        <div class="flex flex-col text-center ml-0 lg:ml-10 mt-10 lg:mt-0">
          <p class="font-bold text-5xl mb-5">
            Upload your image
          </p>
          <p class="text-4xl">
            JPG, GIF or PNG formats that <br> are max. 2000 x 2000 or MB. <br>
            If your image size is bigger,<br> please compress it.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CustomHeadBar from "../components/headbar.vue";
import BrowseButton from "../components/BrowseButton.vue";

export default {
  name: 'Upload',
  components: {
    BrowseButton,
    CustomHeadBar
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
