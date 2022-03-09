function shortcut (string) {
  return string.replace(/[aeiou]/g, "");
}

console.log(shortcut('Hello world how have you been?'));
