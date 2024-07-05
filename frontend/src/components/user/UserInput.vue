<template>
    <div class="text-left group">
        <span class="ml-2 sm:ml-3 md:ml-4 lg:ml-5 xl:ml-7 2xl:ml-8">
            <slot name="placeholder">{{ placeholder }}</slot>
        </span>

        <div class="relative rounded-xl">
            <div class="card h-full w-full rounded-xl invisible group-focus-within:visible"></div>
            <input class="bg-background_konto2-dark border-2 md:border-3 lg:border-4
                rounded-xl placeholder-unselected-default w-full 
                h-10 sm:h-14 md:h-16 lg:h-20 xl:h-24
                px-2 sm:px-3 md:px-4 xl:px-6 2xl:px-7
                focus:ring-0 focus:outline-none focus:border-transparent transition-all duration-100 ease-linear" 
                required :placeholder="placeholder" :type="type">
        </div>
    </div>
</template>

<script>
    export default {
        name: 'UserInput',
        props: {
            placeholder: {
                type: String,
                required: true
            },
            type: {
                type: String,
                default: 'text'
            }
        }
    }
</script>

<style>
    .border-6 {
        border-width: 6px;
    }

    @property --gradient-angle {
        syntax: "<angle>";
        initial-value: 0deg;
        inherits: false;
    }

    .card {
        background: transparent;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
    }


    .card::before,
    .card::after {
        content: "";
        position: absolute;
        inset: -0.25rem;
        z-index: -1;
        background: conic-gradient(
            from var(--gradient-angle),
            #f39c12,
            #ffb300,
            #ffc107,
            #ce93d8,
            #ba68c8,
            #ab47bc,
            #ba68c8,
            #ce93d8,
            #ffc107,
            #ffb300,
            #f39c12);
        border-radius: inherit;
        animation: rotation 10s linear infinite;
    }

    .card::after {
        filter: blur(1.5rem);
    }

    @keyframes rotation {
        0% {
            --gradient-angle: 0deg;
        }
        100% {
            --gradient-angle: 360deg;
        }
    }
</style>
