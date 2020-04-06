/* base-ViTest-viur GULP SCRIPT */

// Project data
var srcpaths = {
	less: './less/**/*.less',
	images: './images/**/*',
	icons: './embedsvg/**/*', //icon- prefix, use Textcolor
	logos: './embedsvg/logos/**/*', //logo- prefix, keep their color
	js:    './js/scripts/**/*.js',
};

var destpaths = {
	css: '../deploy/static/css',
	images: '../deploy/static/images',
	embedsvg: '../deploy/html/embedsvg',
	js: '../deploy/static/js',
};

const gulp = require('gulp');
const plugins = require('gulp-load-plugins');

function loadTask(task, options) {
	return require('./gulptasks/' + task)(gulp, plugins, options)
}

gulp.task('css', loadTask('css_task', {
	src: './less/style.less',
	dest: destpaths.css
}));

gulp.task('icons', loadTask('icon_task', {
	src: [srcpaths.icons],
	dest: destpaths.embedsvg
}));

gulp.task('images', loadTask('image_task', {
	src: srcpaths.images,
	dest: destpaths.images
}));

gulp.task('js', loadTask('js_task', {
	src: srcpaths.js, //scripts to include
	srcFile: './js/app.js', //entrypoint
	dest: destpaths.js //output will be main.(min.)js
}));

gulp.task('lib', loadTask('lib_task', {
	src: [ //register needed libraries, in correct order
		'./js/libs/jquery-3.4.1.min.js',
		'./js/libs/pagination.js',
	],
	dest: destpaths.js
}));

const viBuildTasks = require('./vi/vi_tasks');


gulp.task('watch', () => {
	gulp.watch(srcpaths.less, gulp.series('css'));
	gulp.watch(srcpaths.embedsvg, gulp.series('icons'));
	gulp.watch(srcpaths.images, gulp.series('images'));
});

gulp.task('default', gulp.series(['css', 'images', 'icons', 'js', 'lib', 'vi']));
