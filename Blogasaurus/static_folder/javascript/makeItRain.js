$.fn.makeItRain = function(){

		$(this).click(function(){

			var maxBills = 50;

			for (var i = 0; i < maxBills; i++){
				var random = $(window).width();
				var randomPosition = Math.floor(random*Math.random());
				var randomTime = Math.random() * 40;
				var randomSpeed = (Math.random()*20)+10 ;

				var bills = $("<span class='billsBillsBills'>").css({
					left : randomPosition,
					top: "-150px",
					"-webkit-animation-delay" : randomTime + "s",
					"-webkit-animation-duration" : randomSpeed + "s"
				});

				$(bills).prepend('<img src="/resources/images/bill.svg" alt="a dollar bill">');
				$('body').append(bills);
			}; // end click function
		}); //end for loop
	}; //end make it rain fn.

	$("#rain").makeItRain();

	// thanks to Anisha Varghese from the Noun Project for the SVG!!
