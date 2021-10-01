/* {{app_id}} GULP SCRIPT */

// Project data
var srcpaths = {
	less: './less/**/*.less',
	images: './images/**/*',
	embedsvg: './embedsvg/**/*',
};

var destpaths = {
	css: '../deploy/static/css',
	images: '../deploy/static/images',
	embedsvg: '../deploy/html/embedsvg'
};

// Variables and requirements
const gulp = require('gulp');

const path = require('path');
const del = require('del');
const rename = require('gulp-rename');

const less = require('gulp-less');
const autoprefixer = require('autoprefixer');
const postcss = require('gulp-postcss');
const zindex = require('postcss-zindex');
const focus = require('postcss-focus');
const nocomments = require('postcss-discard-comments');
const cleancss = require('gulp-clean-css');
const jmq = require('gulp-join-media-queries');
const stylefmt = require('gulp-stylefmt');

const imagemin = require('gulp-imagemin');
const cheerio = require('gulp-cheerio');


// compilation and postproduction of LESS to CSS
gulp.task('css', () => {
	del([destpaths.css + '/**/*'], {force: true});

	return gulp.src('./less/style.less')
		.pipe(less({
			paths: [path.join(__dirname, 'less', 'includes')]
		}))
		.pipe(postcss([
			autoprefixer({ // add vendor prefixes
				cascade: false
			}),
			nocomments, // discard comments
			focus, // add focus to hover-states
			zindex, // reduce z-index values
		])) // clean up css
		.pipe(jmq())
		.pipe(stylefmt()) // syntax formatting
		.pipe(gulp.dest(destpaths.css)) // save cleaned version
		.pipe(cleancss()) // minify css
		.pipe(rename({suffix: '.min'}))
		.pipe(gulp.dest(destpaths.css)); // save minified version
});


// reduce images for web
gulp.task('images', () => {
	del([destpaths.images + '/**/*'], {force: true});

	return gulp.src(srcpaths.images)
		.pipe(imagemin([
			imagemin.mozjpeg({progressive: true}),
			imagemin.optipng({optimizationLevel: 5}),
			imagemin.svgo({
				plugins: [
					{removeViewBox: false},
					{removeDimensions: true}
				]
			})
		]))
		.pipe(gulp.dest(destpaths.images));
});

// reduce embedsvg icons for web
gulp.task('embedsvg', () => {
	del([destpaths.embedsvg + '/**/*'], {force: true});

	return gulp.src(srcpaths.embedsvg)
		.pipe(imagemin([
			imagemin.mozjpeg({progressive: true}),
			imagemin.optipng({optimizationLevel: 5}),
			imagemin.svgo({
				plugins: [
					{removeViewBox: false},
					{removeDimensions: true}
				]
			})
		]))
		.pipe(cheerio({
			run: function ($, file) {
				$('style').remove()
				$('[id]').removeAttr('id')
				$('[fill]').removeAttr('fill')
				$('svg').addClass('icon')
			},
			parserOptions: {xmlMode: true}
		}))
		.pipe(rename({prefix: 'icon-'}))
		.pipe(gulp.dest(destpaths.embedsvg));
});


gulp.task('watch', () => {
	gulp.watch(srcpaths.less, gulp.series('css'));
	gulp.watch(srcpaths.embedsvg, gulp.series('embedsvg'));
	gulp.watch(srcpaths.images, gulp.series('images'));
});

gulp.task('default', gulp.series(['css', 'images', 'embedsvg']));
