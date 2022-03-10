// Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence

function replace(s){
  return s.replace(/[aeiou]/gi, '!');  
}

console.log(replace('Hello World!')); // H!ll! W!rld!
