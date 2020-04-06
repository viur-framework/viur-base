module.exports = function (gulp, plugins, options) {

	return function () {
		plugins.del([options.dest + '/**/*',], {force: true});

		return gulp.src(options.src)
			.pipe(plugins.imagemin([
				plugins.imagemin.mozjpeg({progressive: true}),
				plugins.imagemin.optipng({optimizationLevel: 5}),
				plugins.imagemin.svgo({
					plugins: [
						{removeViewBox: false},
						{removeDimensions: true}
					]
				})
			]))
			.pipe(gulp.dest(options.dest));
	}
};
