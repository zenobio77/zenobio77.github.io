$(window).scroll(function() {
    navbar = $('.navbar');
    if($(window).scrollTop() > 200) {
        navbar.addClass('container');
    } else {
      navbar.removeClass('container');
    }
});

$('#parallax1').css({'height': $(window).height()});
$('#parallax2').css({'height': $(window).height()});
