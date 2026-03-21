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
          primary: '#ff4d4d',
          secondary: '#ff7675',
          accent: '#d63031',
          dark: '#0a0505',
          card: '#150a0a',
          glass: 'rgba(255, 77, 77, 0.05)',
        }
      },
      boxShadow: {
        'peixoto': '0 0 20px rgba(255, 77, 77, 0.2)',
        'peixoto-lg': '0 0 40px rgba(255, 77, 77, 0.3)',
      },
      animation: {
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      }
    },
  },
  plugins: [],
}
