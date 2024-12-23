var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
});

jQuery('.top-slider-wrap').owlCarousel({
  loop:true,
  margin:15,
  responsiveClass:true,
  nav:false,
  autoplay:true,
  rtl:true,
  dots:true,
  responsive:{
      0:{
          items:1
      },
      600:{
          items:2
      },
      1000:{
          items:4
      }
  }
});

jQuery(window).scroll(function(){
  if(jQuery(window).scrollTop()>500){
    jQuery('.scroll_top').fadeIn();
  }
  else{
    jQuery('.scroll_top').fadeOut();
  }
});

jQuery('.scroll_top').click(function(){
  jQuery('html,body').animate({scrollTop:0},500);
});

const customCursor = document.getElementById('custom-cursor');
const hoverContainer = document.querySelector('.hover-container');
const updateCursorPosition = (event) => {
  customCursor.style.top = `${event.clientY}px`;
  customCursor.style.left = `${event.clientX}px`;
}
window.addEventListener('mousemove', (event) => {
  updateCursorPosition(event)
  
  if (hoverContainer.matches(':hover')) {
    customCursor.classList.add('zoom')
  } else {
    customCursor.classList.remove('zoom')
  }
})


