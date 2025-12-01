import adapter from '@sveltejs/adapter-auto';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {

		files: {
			lib: 'src/web_application/lib',
			routes: 'src/web_application/routes',
			appTemplate: 'src/web_application/app.html',
			errorTemplate: 'src/web_application/error.html'
		},

		// adapter-auto only supports some environments, see https://svelte.dev/docs/kit/adapter-auto for a list.
		// If your environment is not supported, or you settled on a specific environment, switch out the adapter.
		// See https://svelte.dev/docs/kit/adapters for more information about adapters.
		adapter: adapter()
	}
};

export default config;
