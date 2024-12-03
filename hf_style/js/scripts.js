(function($, document, window){

	$(document).ready(function(){

	    $(".mobile-menu").append($(".main-navigation .menu").clone());
	    $(".toggle-menu").click(function(){
	    	$(".mobile-menu").slideToggle();
	    });
	});
	$(window).ready(function(){
	});

})(jQuery, document, window);