/**
 * Created by rewalkerof on 08.02.18.
 */
$(function () {
    $('.navbar-toggle').click(function () {
        $('.navbar-nav').toggleClass('slide-in');
        $('.side-body').toggleClass('body-slide-in');
        $('#search').removeClass('in').addClass('collapse').slideUp(200);

        /// uncomment code for absolute positioning tweek see top comment in css
        //$('.absolute-wrapper').toggleClass('slide-in');

    });

    // Remove menu for searching
    $('#search-trigger').click(function () {
        $('.navbar-nav').removeClass('slide-in');
        $('.side-body').removeClass('body-slide-in');

        /// uncomment code for absolute positioning tweek see top comment in css
        //$('.absolute-wrapper').removeClass('slide-in');

    });
});

/*fixed heder in table */
// var tableOffset = $("#table-bordered").offset().top;
// var $header = $("#table-bordered > thead").clone();
// var $fixedHeader = $("#header-fixed").append($header);
//
// $(window).bind("scroll", function () {
//     var offset = $(this).scrollTop();
//
//     if (offset >= tableOffset && $fixedHeader.is(":hidden")) {
//         $fixedHeader.show();
//     }
//     else if (offset < tableOffset) {
//         $fixedHeader.hide();
//     }
// });
