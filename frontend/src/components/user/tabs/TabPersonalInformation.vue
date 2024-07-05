<template>
    <div class="w-full h-full content-start text-center 
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

        <div>

        </div>

    </div>
</template>

<script>
import UserInput from '../UserInput.vue';

export default {
    name: 'TabPersonalInformation',
    components: { UserInput },
};
</script>