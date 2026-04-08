/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        peixoto: {
          primary: '#5a8794',
          secondary: '#fd8a0d',
          accent: '#3f5f69',
          dark: '#1a1a2e',
          card: '#16213e',
          glass: 'rgba(90, 135, 148, 0.05)',
        }
      },
      boxShadow: {
        'peixoto': '0 0 20px rgba(90, 135, 148, 0.2)',
        'peixoto-lg': '0 0 40px rgba(90, 135, 148, 0.3)',
      },
      animation: {
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      }
    },
  },
  plugins: [],
}
