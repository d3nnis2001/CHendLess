<template>
    <div class="
    bg-background_konto-dark bg-gradient-to-r from-background_konto2-dark to-background_konto-dark
    rounded-fitting border-gray-400 border-2
    flex items-center justify-center
    ">
        <slot></slot>
    </div>
</template>

<script>
export default {    
    name: 'UserComponent',
};
</script>

<style>
    .rounded-fitting {
        border-radius: 1.35rem;
    }
</style>
