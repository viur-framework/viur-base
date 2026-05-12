const isProd = process.env.NODE_ENV === 'production';
export default ({ ctx }) => ({
	map: isProd ? false : { inline: true },
	plugins: {
    'postcss-import': {},
		'postcss-preset-env': {
			stage: 3,
			features: {
          'custom-media-queries': true,
  		}
		},
		'postcss-sort-media-queries': {},
    'cssnano': isProd ? {} : false,
	}
})
