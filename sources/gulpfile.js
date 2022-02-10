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
	embedsvg: '../deploy/static/svgs'
};

// Variables and requirements
import gulp from 'gulp';
import path from 'path';
globalThis.__dirname = path.dirname(import.meta.url);

import del from 'del';
import rename from 'gulp-rename';
import less from 'gulp-less';
import autoprefixer from 'autoprefixer';
import postcss from 'gulp-postcss'
import zindex from 'postcss-zindex';
import focus from 'postcss-focus';
import nocomments from 'postcss-discard-comments';
import cleancss from 'gulp-clean-css';
import jmq from 'gulp-join-media-queries';
import imagemin from 'gulp-imagemin';
import cheerio from 'gulp-cheerio';

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
