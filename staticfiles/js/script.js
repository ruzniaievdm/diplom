/**
 * Created by rewalkerof on 08.02.18.
 */

(function ($) {
    $(window).on("load", function () {
        $('.coefficient-form').formset({
            addText: 'add coefficient',
            deleteText: 'remove'
        });
    });
})(jQuery);

(function ($) {
    $(window).on("load", function () {
        $('.bp-form').formset({
            addText: 'add work',
            deleteText: 'remove'
        });
    });
})(jQuery);

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

/*function myFunctionFilter() {
 var input, filter, ul, li, a, i;
 input = document.getElementById("myInput");
 filter = input.value.toUpperCase();
 ul = document.getElementById("myUl");
 li = ul.getElementsByTagName("li");
 for (i = 0; i < li.length; i++) {
 a = li[i].getElementsByTagName("a")[0];
 if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
 li[i].style.display = "";
 } else {
 li[i].style.display = "none";

 }
 }
 }*/
