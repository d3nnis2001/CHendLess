module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
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
        background_konto: {
          dark: "#484848"
        },
        green: {
          dark: "#24ff00"
        },
        red: {
          dark: "#ff0000"
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}