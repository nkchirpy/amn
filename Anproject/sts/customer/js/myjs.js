$('.carousel').carousel({
  interval: 3000
})



// index page animation starting


$(document).ready(function () {
      $('#img1').mouseover(function () {
          $(this).fadeTo(100, 0)
      });
      $('#img1').mouseout(function () {
          $(this).fadeTo(0, 100)
      });
  })
  $(document).ready(function () {
        $('#img2').mouseover(function () {
            $(this).fadeTo(100, 0)
        });
        $('#img2').mouseout(function () {
            $(this).fadeTo(0, 100)
        });
    })
    $(document).ready(function () {
          $('#img3').mouseover(function () {
             $(this).fadeTo(100, 0)
          });
          $('#img3').mouseout(function () {
               $(this).fadeTo(0, 100)
          });
      })
      $(document).ready(function () {
            $('#img4').mouseover(function () {
               $(this).fadeTo(100, 0)
            });
            $('#img4').mouseout(function () {
                $(this).fadeTo(0, 100)
            });
        })





// Index page animation ending

// $(window).scroll(function () {
//   $('[id^="box"]').each(function () { // <---loop the divs id starts with #box
//       if (($(this).offset().top - $(window).scrollTop()) < 20) { //<---mark the $(this).offset().top of current object
//           $(this).stop().fadeTo(100, 0); //<----fadeOut the current obj
//       } else {
//           $(this).stop().fadeTo('fast', 1); //<----fadeIn the current obj
//       }
//   });
// });

// tag line blinking starting
// function blink(){
//     $('#tag').delay(2500).fadeTo(0,0).delay(1000).fadeTo(0,2, blink);
// }

// $(document).ready(function() {
//     blink();
// });

// tag line blinking ending


// services page animation ending


// contact page form validation starting
