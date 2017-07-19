function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}

function move(){
  $("pig").css()
}
function pleaseFly(){
  $("#pig").animate({
    "margin-left": "500px"
  });
  $('#pig2').delay(1000);
  $('#pig2').animate({
    "margin-left": "500px"
  });
}

function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#pig").click(pleaseFly);
}

$(document).ready(setup);
