var headerHeight = $('.navbar-nav').height();
var nav = $('.navbar-nav');

$(window).on('scroll', { prevTop: 0 }, function() {
    var currentTop = $(window).scrollTop();

    // User scrolled up?
    if (currentTop < this.prevTop) {
        if (currentTop > 0 && nav.hasClass('hide-nav')) {
            nav.addClass('show-nav');
        } else {
            nav.removeClass('hide-nav show-nav');
        }
    }
    // User scrolled down
    else if (currentTop > this.prevTop) {
        nav.addClass('hide-nav');
    
        if (currentTop > headerHeight && nav.hasClass('show-nav')) {
            nav.removeClass('show-nav');
        }
    }
    this.prevTop = currentTop;
});