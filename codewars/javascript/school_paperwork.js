// Return number of blank pages needed for number of classmates (n) * paperwork pages (m).  If either of the values are equal to or less than 0 return 0. 
// https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd

function paperwork(n, m) {
  if ((n <= 0 || m <= 0)) {
    return 0;
  }
  return n * m;
}function paperwork(n, m) {
  if ((n <= 0 || m <= 0)) {
    return 0;
  }
  return n * m;
}

console.log(paperwork(2, 20)); // 40
console.log(paperwork(3, 0)); // 0
console.log(paperwork(-2, 3)); // 0
