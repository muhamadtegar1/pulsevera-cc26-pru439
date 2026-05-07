/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#E53E3E',
        secondary: '#38A169',
      }
    }
  },
  plugins: []
}
