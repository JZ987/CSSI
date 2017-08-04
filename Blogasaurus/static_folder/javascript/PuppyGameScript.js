var counter = 0;

function move(){
  counter++;
  if(counter < 5){
    $("h2").text("OMG IT MOVED!!!");
  }else{
    $("h2").text("CHASE AFTER IT!!");
  }
  $(".puppy").animate({
    "margin-left": Math.random()*1000 + "px",
    "margin-top": Math.random()*100 + "px"
  })
}

function setup(){
  $(".puppy").click(move);
}

$(document).ready(setup);
