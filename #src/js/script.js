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

if(window.location.pathname=='/'){
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
        
        var delayTop = $('#block1').offset().top;
        
        var scrolls = $(window).scrollTop();
        
        var start = scrolls - delayTop + 125;
        var stop = result + delayTop;

        
        if(start >= 0 && scrolls < stop){
            
            $('.sidebar').css({
              "padding-top": start + "px",
            })
  
        } 

        
  
  
        
    })
  })
  
  
  
  $(window).scroll(function(){
    var blockOne = $('#block1').offset().top
    var heightOne = $('#block1').height()
    var topBlockOne = heightOne + blockOne
  
    var blockTwo = $('#block2').offset().top
    var heighTwo = $('#block2').height()
    var topBlockTwo = blockTwo + heighTwo
  
    var blockTree = $('#block3').offset().top
    var heighTree = $('#block3').height()
    var topBlockTree = blockTree + heighTree
  
    var blockFor = $('#block4').offset().top
    var heighFor = $('#block4').height()
    var topBlockFor = blockFor + heighFor
  
    var blockFive = $('#block5').offset().top
    var heighFive = $('#block5').height()
    var topBlockFive = blockFive + heighFive
  
    var blockSix = $('#block6').offset().top
    var heighSix = $('#block6').height()
    var topBlockSix = blockSix + heighSix
  
    var topScr = $(window).scrollTop() + 150;
    
    if (topScr >= blockOne && topScr <= topBlockOne) {
      $('#link1').addClass('sidebar__link--active')
      $('#dots1').addClass('sidebar__index-dots--active')

  
    } else {
      $('#link1').removeClass('sidebar__link--active')
      $('#dots1').removeClass('sidebar__index-dots--active')
    }
  
    if (topScr >= blockTwo && topScr <= topBlockTwo) {
      $('#link2').addClass('sidebar__link--active')
      $('#dots2').addClass('sidebar__index-dots--active')
  
    } else {
      $('#link2').removeClass('sidebar__link--active')
      $('#dots2').removeClass('sidebar__index-dots--active')
    }
  
    if (topScr >= blockTree && topScr <= topBlockTree) {
      $('#link3').addClass('sidebar__link--active')
      $('#dots3').addClass('sidebar__index-dots--active')
    } else {
      $('#link3').removeClass('sidebar__link--active')
      $('#dots3').removeClass('sidebar__index-dots--active')
    }
  
    if (topScr >= blockFor && topScr <= topBlockFor) {
      $('#link4').addClass('sidebar__link--active')
      $('#dots4').addClass('sidebar__index-dots--active')
  
    } else {
      $('#link4').removeClass('sidebar__link--active')
      $('#dots4').removeClass('sidebar__index-dots--active')
    }
  
    if (topScr >= blockFive && topScr <= topBlockFive) {
      $('#link5').addClass('sidebar__link--active')
      $('#dots5').addClass('sidebar__index-dots--active')
  
    } else {
      $('#link5').removeClass('sidebar__link--active')
      $('#dots5').removeClass('sidebar__index-dots--active')
    }
    if (topScr >= blockSix && topScr <= topBlockSix) {
      $('#link6').addClass('sidebar__link--active')
      $('#dots6').addClass('sidebar__index-dots--active')
  
    } else {
      $('#link6').removeClass('sidebar__link--active')
      $('#dots6').removeClass('sidebar__index-dots--active')
    }
  
   
    
  
          
  })
  


 } else {
  
 }








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



  



$('.block__slider').each(function() { // the containers for all your galleries
    $(this).magnificPopup({
        delegate: 'a', // the selector for gallery item
        type: 'image',
        gallery: {
          enabled:true
        }
    });
});

$('.block__grid').each(function() { // the containers for all your galleries
  $(this).magnificPopup({
      delegate: 'a', // the selector for gallery item
      type: 'image',
      gallery: {
        enabled:true
      }
  });
});

$('.image-link').magnificPopup({type:'image'});



$('.layout__img-link').magnificPopup({type:'image'});
