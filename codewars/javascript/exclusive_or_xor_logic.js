function xor(a, b) {
  if((a === true && b === false)) {
    return true;
  }else if ((a == false && b == true)){
    return true;
  }else{
    return false;
  }
}

// A more elegant solution would have been

function xor_elegant(a, b) {
  return a != b;
}
