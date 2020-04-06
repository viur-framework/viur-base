module.exports = function (gulp, plugins, options) {

	plugins.sourcemaps = require('gulp-sourcemaps');
	plugins.concat = require('gulp-concat');
	plugins.minify = require('gulp-minifier');

	return function () {
		return gulp.src(options.src)
			.pipe(plugins.sourcemaps.init())
			.pipe(plugins.concat("lib.min.js"))
			.pipe(plugins.minify({
				minify: true,
				collapseWhitespace: true,
				conservativeCollapse: true,
				minifyJS: true,
				minifyCSS: true,
				getKeptComment: function (content, filePath) {
					var m = content.match(/\/\*![\s\S]*?\*\//img);
					return m && m.join('\n') + '\n' || '';
				}
			})) // minify
			.pipe(plugins.sourcemaps.write("."))
			.pipe(gulp.dest(options.dest));
	}
};