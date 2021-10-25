$(window).scroll(function() {
    var height = $(window).scrollTop();
    /*Если сделали скролл на 100px задаём новый класс для header*/
    if(height > 56){
        $('.header').addClass('header--fixed');
       
        
    } else{
        /*Если меньше 100px удаляем класс для header*/
        $('.header').removeClass('header--fixed');
        
    }
});

$(window).scroll(function() {
  var height = $(window).scrollTop();
  /*Если сделали скролл на 100px задаём новый класс для header*/
  if(height > 520){
      $('.nav').addClass('nav--fixed');
     
      
  } else{
      /*Если меньше 100px удаляем класс для header*/
      $('.nav').removeClass('nav--fixed');
      
  }
});


$(".toggle-menu").click(function(e) {
    e.preventDefault();
    $(".menu-btn").toggleClass('menu-btn_active');
    $(".header__drop").toggleClass('header__drop--active');

})
$(".header__drop").mouseleave(function() {
    $(".menu-btn").removeClass('menu-btn_active');
    $(".header__drop").removeClass('header__drop--active');
});


$(".toggle-menu-2").click(function(e) {
  e.preventDefault();
  $(".menu-btn-2").toggleClass('menu-btn-2_active');
  $(".header").toggleClass('header--active');

  

});
  
jQuery(document).ready(function($) {
    var url=document.location.href;
    $.each($(".header__link"),function(){
        if(this.href==url){
            $(this).addClass('header__link--active');
        }
    });
});



$('.callback-show').click(function(e){
  e.preventDefault();

  $('.popup-call').addClass('popup-call--active')

});

$('.popup-call__closer, .popup-call__close').click(function(e){
  e.preventDefault();

  $('.popup-call').removeClass('popup-call--active')

});

$(document).ready(function(){
  var heights = [];  

  $(".block").each(function(indx, element){
    heights.push($(element).height());
    
  });
  
  var a = heights; 
  var result=0;
  $.each(a, function(ind,val){
    result+=val;
  });

  

  $(window).scroll(function(){
      var header = $('.header').height();
      var slide = $('.slide').height();
      var nav = $('.nav').height();
      var grid = $('.grid').height();
      var sidebar = $('.sidebar').height();
      var delayTop = header + slide + nav + grid;
      
      var scrolls = $(window).scrollTop();
      
      var start = scrolls - delayTop;
      var stop = result + delayTop + 400 ;
      
    
      
      if(start >= 0 && scrolls < stop - sidebar){
          
          $('.sidebar').css({
            "padding-top": start + "px",
          })

      } 
      
  })
})







$('.block__slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    infinite: true,

    fade: true,
    asNavFor: '.block__slider-nav',
    prevArrow: "<div class='arrow-wrap prev'><img src='/static/images/icons/arrow.svg' alt=''></div>",
    nextArrow: "<div class='arrow-wrap next'><img src='/static/images/icons/arrow.svg' alt=''></div>",
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



  $('.layout__slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    infinite: true,
    swipe: false,

    fade: true,
    asNavFor: '.layout__nav',
    arrows: false,
    
  });
  $('.layout__nav').slick({
    slidesToShow: 3,
    infinite: true,

    slidesToScroll: 1,
    asNavFor: '.layout__slider',
    dots: false,
    arrows: false,
    centerMode: true,
    focusOnSelect: true,
    swipe: false,
  });