// Adapted/edited from http://www.simonbattersby.com/

function cycleImages(){
      var $active = $('#background_cycler .active');
      var $next = ($('#background_cycler .active').next().length > 0)
				? $('#background_cycler .active').next()
				: $('#background_cycler img:first');
      $next.css('z-index', 2);
	  $active.fadeOut(1500,function(){
	  $active.css('z-index', 1).show().removeClass('active');
      $next.css('z-index', 3).addClass('active');
    });
}

    $(window).load(function(){
		$('#background_cycler').fadeIn(1500);
		  setInterval('cycleImages()', 5500);
    })

// Band cart

simpleCart.currency({
    code: "ZAR",
    name: "Rand",
    symbol: "R",
    delimiter: " ",
    decimal: ",",
    after: false,
    accuracy: 2
  });
simpleCart({
    checkout: {
      type: "PayPal",
      email: "someone@gmail.com"
    },
    cartStyle: "table"
  });
