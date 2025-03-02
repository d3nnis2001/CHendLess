const plugin = require('tailwindcss/plugin')
const { h } = require('vue')

module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      height: {
        100: '25rem',
        125: '31.25rem',
        150: '37.5rem',
        200: '50rem',
      },
      textShadow: {
        sm: '0 1px 2px var(--tw-shadow-color)',
        DEFAULT: '0 2px 4px var(--tw-shadow-color)',
        md: '0 4px 8px var(--tw-shadow-color)',
        lg: '0 8px 16px var(--tw-shadow-color)',
        none: 'none',
      },
      fontSize: {
        'ssm': '10px',
        '10xl': '135px',
      },
      colors: {
        primary: {
          dark: "#1B1B1B",
        },
        white: {
          dark: "#FFFFFF"
        },
        black : {
          dark: "#000000"
        },
        background_rec: {
          dark: "#323232"
        },
        background_rec2: {
          dark: "#3c3c3c"
        },
        background_konto: {
          dark: "#484848"
        },
        background_konto2: {
          dark: "#585858"
        },
        green: {
          dark: "#24ff00"
        },
        red: {
          dark: "#ff0000"
        },
        unselected: {
          default: "#AFAFAF"
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      keyframes: {
        slidein: {
          from: {
            opacity: "0",
            transform: 'translateX(-10px)',
          },
          to: {
            opacity: "1",
            transform: 'translateX(0)',
          },
        },
        gradient: {
          '0%': {
            backgroundPosition: '0% 50%',
          },
          '100%': {
            backgroundPosition: '100% 50%',
          },
        },
        gradient_vbar: {
          '0%': {
            backgroundPosition: '50% 100%',
          },
          '100%': {
            backgroundPosition: '50% 0%',
          }
        }
      },
      animation: {
        gradient: 'gradient 6s linear infinite',
        gradient_vbar: 'gradient_vbar 6s linear infinite',
        slidein: 'slidein 1s ease var(--slidein-delay, 0) forwards'
      },
    },
  },
  plugins: [
    plugin(function ({ matchUtilities, theme }) {
      matchUtilities(
        {
          'text-shadow': (value) => ({
            textShadow: value,
          }),
        },
        { values: theme('textShadow') }
      )
    }),
  ],
}