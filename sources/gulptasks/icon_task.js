module.exports = function (gulp, plugins, options) {
	plugins.rename = require('gulp-rename');
	plugins.cheerio = require('gulp-cheerio');
	plugins.del = require('del');
	plugins.imagemin = require('gulp-imagemin');
	plugins.flatten = require('gulp-flatten');
	plugins.filter = require("gulp-filter");

	gulp.task('icons_clean', function () {
		plugins.del([options.dest + '/**/*.svg'], {force: true})
		return gulp.src(options.src)
		}
	)

	gulp.task('icons-build', function () {

		return gulp.src(options.src)
			.pipe(plugins.filter(['**/*.svg','!*/logos/**','!*/**/logos/**'])) // alles außer logos
			//.pipe(plugins.print())
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
			.pipe(plugins.cheerio({
				run: function ($, file) {
					$('style').remove();
					$('title').remove();
					$('[id]').removeAttr('id');
					//$('[class]').removeAttr('class')
					//$('[fill]').removeAttr('fill');
					$('svg').addClass('icon').removeAttr("x").removeAttr("y");
				},
				parserOptions: {xmlMode: true}
			}))
			.pipe(plugins.rename(function(path){
				if (path.extname) {
					if (path.dirname === '.') {
						path.dirname = 'icons';
					}
					path.basename = path.dirname + '-' + path.basename;
					path.dirname = '';
				}
			}))
			.pipe(plugins.flatten())
			.pipe(gulp.dest(options.dest));
		}
	);

	gulp.task('logos-build', function () {

		return gulp.src(options.src) //.concat(['!./**/embedsvg/**/*','./**/embedsvg/logos/*']) destroys ordering ---<
			.pipe(plugins.filter(['embedsvg/logos/**','**/embedsvg/logos/**']))
			//.pipe(plugins.print())
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
			.pipe(plugins.cheerio({
				run: function ($, file) {
					$('svg').addClass('logo').removeAttr('x').removeAttr('y');
				},
				parserOptions: {xmlMode: true}
			}))
			.pipe(plugins.rename(function(path){
				if (path.extname) {
					if (path.dirname === '.') {
						path.dirname = 'icons';
					}
					path.basename = path.dirname + '-' + path.basename;
					path.dirname = '';
				}
			}))
			.pipe(plugins.flatten())
			.pipe(gulp.dest(options.dest));
		}
	);

	return gulp.series([
		'icons_clean',
		'icons-build',
		'logos-build'
	])
};
