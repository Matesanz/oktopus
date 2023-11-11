const tailwindcss = require('tailwindcss');
const autoprefixer = require('autoprefixer');
const { default: postcss } = require('postcss');

const config = {
	plugins: [
		//Some plugins, like tailwindcss/nesting, need to run before Tailwind,
		tailwindcss(),
		//But others, like autoprefixer, need to run after,
		autoprefixer,
		postcss()
	]
};

module.exports = config;
