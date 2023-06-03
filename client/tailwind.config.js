module.exports = {
    content: ["./src/**/*.{js,jsx,ts,tsx}", "./public/index.html"],
    theme: {
        extend: {
          backgroundImage: {
            'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
          }
        },
    },
    plugins: [require('tailwindcss-font-inter')],
    variants: {},
    corePlugins: {
        preflight: true,
    },
};