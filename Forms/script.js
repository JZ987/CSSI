function greeting(){
  var userName = $('#username').val();
  /*alert("Hi " + userName + "! Welcome to this website!!");*/
  $("h2").text("Hello, " + userName + "!!");
}

function setup(){
  $('#ok_button').click(greeting);
}

$(document).ready(setup);
