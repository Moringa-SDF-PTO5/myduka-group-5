/** @type {import('tailwindcss').Config} */
import { colors } from '@mui/material'
import daisyui from 'daisyui'

export default {
    content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
    theme: {
        extend: {
            fontFamily: {
                sans: ['roboto', 'sans-serif'],
            },
            colors: {
                'edit-blue': '#2E6C7F',
                'delete-red': '#E93434',
            },
        },
    },
    plugins: [require('daisyui')],
}
