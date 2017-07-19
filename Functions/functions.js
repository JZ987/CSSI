function salesTax(total){
  return Math.round((total + total * 0.095) * 100) / 100;
}

function taxAndTip(bill, tax, tip){
  var afterTax = bill * (1 + tax / 100);
  var afterTip = afterTax * (1 + tip / 100);
  return afterTip;
}
