function move(){
  $("h2").text("OMG IT MOVED!!! TRY CHASING AFTER IT!!")
  $(".puppy").animate({
    "margin-left": Math.random()*1000 + "px"
  })
  $(".puppy").animate({
    "margin-top": Math.random()*100 + "px"
  })
}

function setup(){
  $(".puppy").click(move);
}

$(document).ready(setup);
