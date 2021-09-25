$(window).scroll(function () {
  var height = $(window).scrollTop();
  /*Если сделали скролл на 100px задаём новый класс для header*/

  if (height > 56) {
    $('.header').addClass('header--fixed');
  } else {
    /*Если меньше 100px удаляем класс для header*/
    $('.header').removeClass('header--fixed');
  }
});
$(window).scroll(function () {
  var height = $(window).scrollTop();
  /*Если сделали скролл на 100px задаём новый класс для header*/

  if (height > 520) {
    $('.nav').addClass('nav--fixed');
  } else {
    /*Если меньше 100px удаляем класс для header*/
    $('.nav').removeClass('nav--fixed');
  }
});
$(".toggle-menu").click(function (e) {
  e.preventDefault();
  $(".menu-btn").toggleClass('menu-btn_active');
  $(".header__drop").toggleClass('header__drop--active');
});
jQuery(document).ready(function ($) {
  var url = document.location.href;
  $.each($(".header__link"), function () {
    if (this.href == url) {
      $(this).addClass('header__link--active');
    }
  });
});
$(document).ready(function () {
  var heights = [];
  $(".block").each(function (indx, element) {
    heights.push($(element).height());
  });
  var a = heights;
  var result = 0;
  $.each(a, function (ind, val) {
    result += val;
  });
  $(window).scroll(function () {
    var header = $('.header').height();
    var slide = $('.slide').height();
    var nav = $('.nav').height();
    var grid = $('.grid').height();
    var sidebar = $('.sidebar').height();
    var delayTop = header + slide + nav + grid;
    var scrolls = $(window).scrollTop();
    var start = scrolls - delayTop;
    var stop = result + delayTop;

    if (start >= 0 && scrolls < stop - sidebar) {
      $('.sidebar').css({
        "padding-top": start + "px"
      });
    }
  });
}); // var postion = $('#block-1').offset().top,
//     height = $('#block-1').height();
// $(document).on('scroll', function (){
//   var scroll = $(document).scrollTop();
//   if(scroll  > postion && scroll < (postion + height) ) {
//      $('#link-1').addClass('sidebar__link--active')
//      }else {
//         $('#link-1').removeClass('sidebar__link--active ')
//      }
// })

$('.block__slider').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  infinite: true,
  fade: true,
  asNavFor: '.block__slider-nav',
  prevArrow: "<div class='arrow-wrap prev'><img src='/static/images/icons/arrow.svg' alt=''></div>",
  nextArrow: "<div class='arrow-wrap next'><img src='/static/images/icons/arrow.svg' alt=''></div>"
});
$('.block__slider-nav').slick({
  slidesToShow: 6,
  infinite: true,
  slidesToScroll: 1,
  asNavFor: '.block__slider',
  dots: false,
  arrows: false,
  centerMode: true,
  focusOnSelect: true
});