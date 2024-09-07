<!-- TODO: Add button functionality (and outlines) and proper tel number shit -->

<template>
    <div class="w-full h-full content-stretch text-center 
    grid xl:grid-rows-5 xl:gap-8
    grid-flow-row items-start gap-2 sm:gap-4 md:gap-6">

        <div>
            <span class="text-white-dark font-semibold text-shadow-md shadow-neutral-800 text-xl sm:text-3xl md:text-4xl lg:text-6xl xl:text-7xl 2xl:text-8xl">
                Personal Information
            </span>
        </div>

        <div class="content-center w-full h-full grid grid-rows-2 lg:grid-rows-none lg:grid-cols-2 gap-2 md:gap-4 lg:gap-6">
            <UserInput placeholder="First Name"/>
            <UserInput placeholder="Last Name"/>
        </div>

        <div>
            <UserInput placeholder="Email" type="email"/>
        </div>

        <div class="content-center w-full h-full grid grid-rows-2 lg:grid-rows-none lg:grid-cols-2 gap-2 md:gap-4 lg:gap-6">
            <UserInput placeholder="Telephone" type="tel"/>
            <UserInput placeholder="Birthday" type="date"/>
        </div>

        <div class="w-full h-full flex flex-row gap-2 md:gap-4 lg:gap-6">
            <PurpleYellowButton class="rounded-xl">
                Save
            </PurpleYellowButton>            
            <button class="border-2 md:border-3 lg:border-4 rounded-xl bg-background_konto2-dark relative text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium text-sm px-7 md:px-14 lg:px-20 py-2.5 text-center h-fit w-fit md:text-3xl">
                Cancel
            </button>
        </div>

    </div>
</template>

<script>
import UserInput from '../UserInput.vue';
import PurpleYellowButton from '../../purpleYellowButton.vue';

export default {
    name: 'TabPersonalInformation',
    components: { UserInput, PurpleYellowButton },
};
</script>