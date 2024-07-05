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
                                    <svg class="h-14 w-14 sm:h-24 sm:w-24 md:h-32 md:w-32 lg:h-44 lg:w-44 rounded-full flex-shrink-0 fill-slate-50" viewBox="0 0 38 37" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M7.72484 27.85C9.28317 26.6583 11.0248 25.7187 12.9498 25.0312C14.8748 24.3437 16.8915 24 18.9998 24C21.1082 24 23.1248 24.3437 25.0498 25.0312C26.9748 25.7187 28.7165 26.6583 30.2748 27.85C31.3443 26.5972 32.1769 25.1763 32.7728 23.5875C33.3686 21.9986 33.6665 20.3027 33.6665 18.5C33.6665 14.4361 32.238 10.9757 29.3811 8.11871C26.5241 5.26176 23.0637 3.83329 18.9998 3.83329C14.9359 3.83329 11.4755 5.26176 8.61859 8.11871C5.76164 10.9757 4.33317 14.4361 4.33317 18.5C4.33317 20.3027 4.63109 21.9986 5.22692 23.5875C5.82275 25.1763 6.65539 26.5972 7.72484 27.85ZM18.9998 20.3333C17.1971 20.3333 15.6769 19.7145 14.4394 18.477C13.2019 17.2395 12.5832 15.7194 12.5832 13.9166C12.5832 12.1138 13.2019 10.5937 14.4394 9.35621C15.6769 8.11871 17.1971 7.49996 18.9998 7.49996C20.8026 7.49996 22.3228 8.11871 23.5603 9.35621C24.7978 10.5937 25.4165 12.1138 25.4165 13.9166C25.4165 15.7194 24.7978 17.2395 23.5603 18.477C22.3228 19.7145 20.8026 20.3333 18.9998 20.3333ZM18.9998 36.8333C16.4637 36.8333 14.0804 36.352 11.8498 35.3895C9.61928 34.427 7.679 33.1208 6.029 31.4708C4.379 29.8208 3.07275 27.8805 2.11025 25.65C1.14775 23.4194 0.666504 21.0361 0.666504 18.5C0.666504 15.9638 1.14775 13.5805 2.11025 11.35C3.07275 9.1194 4.379 7.17913 6.029 5.52913C7.679 3.87913 9.61928 2.57288 11.8498 1.61038C14.0804 0.647876 16.4637 0.166626 18.9998 0.166626C21.5359 0.166626 23.9193 0.647876 26.1498 1.61038C28.3804 2.57288 30.3207 3.87913 31.9707 5.52913C33.6207 7.17913 34.9269 9.1194 35.8894 11.35C36.8519 13.5805 37.3332 15.9638 37.3332 18.5C37.3332 21.0361 36.8519 23.4194 35.8894 25.65C34.9269 27.8805 33.6207 29.8208 31.9707 31.4708C30.3207 33.1208 28.3804 34.427 26.1498 35.3895C23.9193 36.352 21.5359 36.8333 18.9998 36.8333ZM18.9998 33.1666C20.6193 33.1666 22.1471 32.9298 23.5832 32.4562C25.0193 31.9826 26.3332 31.3027 27.5248 30.4166C26.3332 29.5305 25.0193 28.8507 23.5832 28.377C22.1471 27.9034 20.6193 27.6666 18.9998 27.6666C17.3804 27.6666 15.8526 27.9034 14.4165 28.377C12.9804 28.8507 11.6665 29.5305 10.4748 30.4166C11.6665 31.3027 12.9804 31.9826 14.4165 32.4562C15.8526 32.9298 17.3804 33.1666 18.9998 33.1666ZM18.9998 16.6666C19.7943 16.6666 20.4512 16.4069 20.9707 15.8875C21.4901 15.368 21.7498 14.7111 21.7498 13.9166C21.7498 13.1222 21.4901 12.4652 20.9707 11.9458C20.4512 11.4263 19.7943 11.1666 18.9998 11.1666C18.2054 11.1666 17.5484 11.4263 17.029 11.9458C16.5096 12.4652 16.2498 13.1222 16.2498 13.9166C16.2498 14.7111 16.5096 15.368 17.029 15.8875C17.5484 16.4069 18.2054 16.6666 18.9998 16.6666Z"/>
                                    </svg>
                                </div>
                                <span class="text-center font-bold text-md sm:text-base md:text-xl lg:text-3xl xl:text-4xl 2xl:text-5xl">
                                    {{ $route.params.id }}
                                </span>

                            </div>
                        </div>
                    </UserComponent>

                    <UserComponent class="h-full">
                        <UserTab @tab-change="handleTabChange"></UserTab>
                    </UserComponent>
                    
                </div>
                <!-- 75% Column -->
                <div class="h-full content-center py-4 sm:py-5 md:py-6 lg:py-7 xl:py-8 2xl:py-9">
                    <UserComponent class="grid mr-4 sm:mr-5 md:mr-6 lg:mr-7 xl:mr-8 2xl:mr-9 justify-center min-h-full ">
                        <component :is="currentTabComponent" class="w-full animate-slidein [--slidein-delay:100ms] opacity-0 sm:py-2 md:py-6 lg:py-8 xl:py-10"></component>
                    </UserComponent>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import CustomHeadBar from "../components/headbar.vue";
import UserComponent from "../components/user/UserComponent.vue";
import UserTab from "../components/user/UserTab.vue";
import TabHistory from "../components/user/tabs/TabHistory.vue";
import TabPersonalInformation from "../components/user/tabs/TabPersonalInformation.vue";
import TabStatistics from "../components/user/tabs/TabStatistics.vue";
import TabSubscription from "../components/user/tabs/TabSubscription.vue";
import TabAccount from "../components/user/tabs/TabAccount.vue";

export default {
    name: 'User',
    components: { CustomHeadBar, UserComponent, UserTab, TabPersonalInformation, TabHistory, TabStatistics, TabSubscription, TabAccount },
    data() {
        return {
            currentTabComponent: 'TabPersonalInformation' // Initial default component
        };
    },
    methods: {
        handleTabChange(tabTarget) {
            switch (tabTarget) {
                case 'history':
                    this.currentTabComponent = 'TabHistory';
                    break;
                case 'personal':
                    this.currentTabComponent = 'TabPersonalInformation';
                    break;
                case 'statistics':
                    this.currentTabComponent = 'TabStatistics';
                    break;
                case 'subscription':
                    this.currentTabComponent = 'TabSubscription';
                    break;
                case 'account':
                    this.currentTabComponent = 'TabAccount';
                    break;
                case 'none':
                    this.currentTabComponent = this.currentTabComponent;
                default:
                    this.currentTabComponent = 'TabPersonalInformation';
            }
        }
    }
};
</script>

<style>
/* * { 
  border: 1px solid red; 
} */
</style>