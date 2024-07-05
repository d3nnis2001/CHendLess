<template>
    <div 
        :class="['flex items-center duration-100 ease-in w-full justify-center md:w-fit', activeClass]"
        @click="handleClick"
        @keyup.enter="handleClick"
        :data-tab-target="tabTarget"
        role="button"
        tabindex="0">
        
        <svg class="h-10 w-10 flex-none fill-current" :viewBox="viewBox" xmlns="http://www.w3.org/2000/svg">
            <path :d="svgpath"/>
        </svg>

        <span class="ml-2 hidden md:block">
            <slot></slot>
        </span>
    </div>
</template>

<script>
export default {
    name: 'UserTabTextImage',

    props: {
        svgpath: {
            type: String,
            required: true
        },
        viewBox: {
            type: String,
            required: true
        },
        tabTarget: {
            type: String,
            required: true
        },
        active: {
            type: Boolean,
            default: false
        },
        logOut: {
            type: Boolean,
            default: false,
            required: false
        }
    },

    computed: {
        activeClass() {
            if (this.logOut) return 'hover:text-[#FF4E4E] text-[#fa2828] font-semibold';
            return this.active ? 'text-white-dark' : 'text-unselected-default hover:text-white-dark';
        },
        showBar() {
            return this.active && !this.logOut;
        }
    },

    methods: {
        handleClick() {
            this.$emit('tab-click', this.tabTarget);
        }
    }
};
</script>