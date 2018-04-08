(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();

    $('#sidenavcontainer').pushpin({


        top: $('#sidenavcontainer').offset().top + 50,
        offset : 120,
        bottom: ($(document).height() - 795),
        //bottom: $('#sidenavcontainer').offset().top + 800,
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