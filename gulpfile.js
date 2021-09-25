/**
 * General variables
 */

const gulp = require('gulp'),
    csso = require('gulp-csso'),
    browserSync = require('browser-sync'),
    autoprefixer = require('gulp-autoprefixer'),
    sass = require('gulp-sass'),
    tildeImporter = require('node-sass-tilde-importer'),
    del = require('del'),
    babel = require('gulp-babel'),
    imagemin = require('gulp-imagemin');
    uglify      = require('gulp-uglify');

// Build settings

let srcPath = './#src/sass';
let devPath = './static/css';
let distPath = './static/css';
let soutcePath = './#src/js';
let jsDistPath = './static/js';
let imagesPath = './#src/images/';
let imagesDestPath = './static/images'


/**
 * Browser Sync Init
 */

function runServer() {
    var proc = exec('python manage.py runserver')
}

// gulp.task('browserSync', ['runserver'], function() {
    
// });

function browser(runServer) {
    browserSync.init({
        notify: false,
        port: 3000,
        proxy: 'localhost:8000'
    })
}



/**
 * Build styles
 */

function buildStyles() {

        return gulp.src(srcPath + '/*.scss')
            .pipe(sass({
                importer: tildeImporter
            }).on('error', onError))
            .pipe(autoprefixer({overrideBrowserslist: ['last 100 versions'], cascade: true}))
            .pipe(gulp.dest(distPath))
            .pipe(csso({
                comments: true
            }))
            // .pipe(rename({suffix: '.min', prefix: ''}))
            .pipe(gulp.dest(distPath))
            .pipe(browserSync.stream());

}

function buildJs() {
    return gulp.src(soutcePath + '/*.js')
    
        .pipe(babel({
            plugins: ['@babel/transform-runtime']
        }))
        // .pipe(uglify())
        .pipe(gulp.dest(jsDistPath))
        .pipe(browserSync.stream());


}

// function images() {
//     return gulp.src(imagesPath + '/**/*.+(png|jpg|gif|svg|jpeg)')
//     .pipe(imagemin({
        
//     }))
//     .pipe(gulp.dest(imagesDestPath))
//     .pipe(browserSync.stream());
// }



/**
 * Reload browser
 */



/**
 * General watcher
 */

function watch() {
    gulp.watch([srcPath + '/*.scss'], gulp.series(buildStyles));
    gulp.watch([soutcePath + '/*.js'], gulp.series(buildJs));
    // gulp.watch([imagesPath + '/**/*.+(png|jpg|gif|svg|jpeg)'], gulp.series(images));
    gulp.watch('./main/templates/**/*.html', browserSync.reload); 
}



/**
 * Clean dist
 */
// function cleanDist(cb) {
//     del.sync([distPath]);
//     cb();
// }

/**
 * Clean dev
 */
function cleanDev(cb) {
    del.sync([devPath]);
    // del.sync([imagesDestPath]);
   
    cb();
}

// Error handler

function onError(err) {
    console.log(err);
    this.emit('end');
}

/**
 * Gulp Start
 */

exports.default = gulp.series(cleanDev, buildStyles, buildJs, gulp.parallel(browser, watch));
