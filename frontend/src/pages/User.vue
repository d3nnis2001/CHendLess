<template>
    <div class="flex flex-col h-screen">
        <CustomHeadBar :profileInsteadOfButton="true"></CustomHeadBar>
        <div class="flex-grow flex items-center justify-center my-4 sm:my-8 md:my-12 xl:my-16 2xl:my-20">
            <div class="h-full items-center justify-center w-11/12 border-2 rounded-3xl border-gray-400
            bg-background_rec-dark bg-gradient-to-r from-background_rec2-dark to-background_rec-dark
            grid grid-cols-[1fr_3fr] text-sm sm:text-base md:text-lg lg:text-2xl xl:text-3xl 2xl:text-4xl
            gap-4 sm:gap-5 md:gap-6 lg:gap-7 xl:gap-8 2xl:gap-9">
                <!-- 25% Column -->
                <div class="h-full grid grid-rows-[1fr_2fr] gap-4 sm:gap-5 md:gap-6 lg:gap-7 xl:gap-8 2xl:gap-9">
                    <UserComponent>
                        <div class="flex justify-center items-center h-full w-full">
                            <div class="flex flex-col items-center h-full w-full justify-center">
                                <div class="mb-4 relative">
                                    <div class="absolute inset-0 hover:bg-black-dark hover:bg-opacity-20 rounded-full transition-all duration-200 ease-in"></div>
                                    <img src="../assets/profile.svg" alt="User Image" class="h-14 w-14 sm:h-24 sm:w-24 md:h-32 md:w-32 lg:h-44 lg:w-44 rounded-full">
                                </div>
                                <span class="text-center font-bold text-md sm:text-base md:text-xl lg:text-3xl xl:text-4xl 2xl:text-5xl">
                                    User {{ $route.params.id }}
                                </span>
                            </div>
                        </div>
                    </UserComponent>

                    <UserComponent>
                        User {{ $route.params.id }}
                    </UserComponent>
                    
                </div>
                <!-- 75% Column -->
                <div class="h-full content-center py-4 sm:py-5 md:py-6 lg:py-7 xl:py-8 2xl:py-9">
                    <UserComponent class="grid mr-4 sm:mr-5 md:mr-6 lg:mr-7 xl:mr-8 2xl:mr-9 justify-center min-h-full">
                        User {{ $route.params.id }}
                    </UserComponent>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import CustomHeadBar from "../components/headbar.vue";
import UserComponent from "../components/UserComponent.vue";

export default {
    name: 'User',
    components: { CustomHeadBar, UserComponent }
};
</script>

<style>
/* * { 
  border: 1px solid red; 
} */
</style>