function salesTax(total){
  return Math.round((total + total * 0.095) * 100) / 100;
}

function taxAndTip(bill, tax, tip){
  var afterTax = bill * (1 + tax / 100);
  var afterTip = afterTax * (1 + tip / 100);
  return afterTip;
}

function skeeballRating(score){
  if(score < 150){
    alert("pretty bad");
  }else if(150 <= score && score < 250){
    alert("decent");
  }else if(250 <= score && score < 350){
    alert("good");
  }else if(350 <= score && score < 450){
    alert("great");
  }else if(450 <= score){
    alert("pretty hard to do");
  }
}

function reverse(){
  var groceries = ['apple', 'banana', 'orange', 'pineapple'];
  var reverse = [];
  reverse.push(groceries.pop());
  reverse.push(groceries.pop());
  reverse.push(groceries.pop());
  reverse.push(groceries.pop());
  return reverse;
}

function arrayDoubled(){
  var originalArray = [1,2,3,4]
  for(var i = 0; i < originalArray.length; i++){
    alert(originalArray[i]*2);
  }
}

function merge(){
  var numbers = [1,2,3]
  var letters = ["a", "b", "c", "d", "e"]
  var len = numbers.length;
  var combined = []
  for(var i = 0; i < len; i++){
    combined.push(numbers.shift());
    combined.push(letters.shift());
  }
  return combined.concat(letters);
}

function findLongestLength(array){
    var longestLength = array[0].length;
    for(var i = 1; i < array.length; i++){
      if(array[i].length > longestLength){
        longestLength = array[i].length;
      }
    }
    return longestLength;
}

function wordsInABox(array){
  var longestLength = findLongestLength(array);
  var lengthOfTopAndBottom = longestLength+4;
  var dashes = "";
  for(var i = 0; i < lengthOfTopAndBottom; i++){
    dashes += "-";
  }
  console.log(dashes);
  var words = "";
  for(var i = 0; i < array.length; i++){
    var leftOverLength = lengthOfTopAndBottom - array[i].length - 3;
    words = "| " + array[i];
    for(var j = 0; j < leftOverLength; j++){
      words += " ";
    }
    words += "|";
    console.log(words);
  }
  console.log(dashes);
}

function stringToMorse(string){
  var morseCode = ["/",".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                    "...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--...",
                    "---..","----.","-----"];
  var lettersAndNumbers = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                            '1','2','3','4','5','6','7','8','9','0'];
  var output = "";
  for(var i = 0; i < string.length; i++){
    var char = string.charAt(i).toLowerCase();
    var index = lettersAndNumbers.indexOf(char);
    output += morseCode[index] + " ";
  }
  console.log(output);
}

function square(number){

}
