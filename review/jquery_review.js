function changeColor(){
    var ran = Math.round(Math.random()*10);
    if(ran == 0){
      $(this).css("background-color", "green");
    }else if(ran == 1){
      $(this).css("background-color", "blue");
    }else if(ran == 2){
      $(this).css("background-color", "yellow");
    }else if(ran == 3){
      $(this).css("background-color", "purple");
    }else if(ran == 4){
      $(this).css("background-color", "orange");
    }else if(ran == 5){
      $(this).css("background-color", "lime");
    }else if(ran == 6){
      $(this).css("background-color", "aqua");
    }else if(ran == 7){
      $(this).css("background-color", "fuchsia");
    }else if(ran == 8){
      $(this).css("background-color", "FF7474");
    }else if(ran == 9){
      $(this).css("background-color", "green");
    }
}

function change(){
    $(this).css("background-color", "black");
    $(this).animate({
      "height": "500px",
      "width": "500px"
    })
}

function changeBack(){
  $(this).css("background-color", "green");
  $(this).animate({
    "height": "300px",
    "width": "300px"
  })
}

function changeName(){
  var userName = $("#username").val();
  $("span").text(userName + "!!");
}

function setup(){
  //$("body").append("<div></div>");
  $("#ok_button").click(changeName);
  $("body").click(changeColor);
  $('#items').keypress(function(e){
      if(e.keyCode == 13){
        e.preventDefault();
        var item = $("#items").val();
        $("h3").append(item + "<br>");
        $("#items").val("");
      }
  });
  //$("div").mouseenter(change);
  //$("div").mouseleave(changeBack);
}

$(document).ready(setup);
