<template>
    <footer class="w-full h-20 md:h-40 lg:h-48 rounded-t-3xl text-center">
        <div class="grid grid-cols-[1fr_3fr] gap-2 md:gap-4 h-full items-center justify-items-center">
            <!-- 25% Column -->
            <div>
                <span class="self-center font-bold whitespace-nowrap text-sm sm:text-lg md:text-3xl lg:text-4xl xl:text-5xl 2xl:text-6xl">CHendLess</span>
            </div>
            <!-- 75% Column -->
            <div class="grid grid-cols-2 grid-rows-2 md:flex w-full h-full items-center justify-around font-medium text-ssm sm:text-base md:text-lg lg:text-2xl xl:text-3xl 2xl:text-4xl">
                <div>
                    <a href="https://www.tiktok.com/explore" target="_blank" rel="noopener noreferrer" class="hover:underline">
                        <span>TikTok</span>
                    </a>
                </div>
                <div>
                    <a href="https://www.instagram.com" target="_blank" rel="noopener noreferrer" class="hover:underline">
                        <span>Instagram</span>
                    </a>
                </div>
                <div>
                    <RouterLink to="/datenschutz" class="hover:underline">
                        <span>Datenschutzerklärung</span>
                    </RouterLink>
                </div>
                <div>
                    <RouterLink to="/impressum" class="hover:underline">
                        <span>Impressum</span>
                    </RouterLink>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>
  export default {
    name: 'Impressum'
  };
</script>