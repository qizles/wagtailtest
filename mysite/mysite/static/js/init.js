(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();
    $('#columniwannapush').pushpin({
        top: $('#columniwannapush').offset().top,
        //bottom: columniwannapush.offset().top + columniwannapush.outerHeight() - columniwannapush.height()
    });



  }); // end of document ready
})(jQuery); // end of jQuery name space





 //$(document).ready(function(){
//    $('.pushpin').pushpin({
//      top: 1000,
//      offset: 400
//    });
//  });