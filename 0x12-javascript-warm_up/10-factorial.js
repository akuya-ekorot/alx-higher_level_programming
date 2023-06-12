#!/usr/bin/node

let number;

function factorial (n) {
  if (n === 0) {
    return 1;
  }

  return n * factorial(n - 1);
}

if (parseInt(process.argv[2])) {
  number = process.argv[2];
} else {
  number = 0;
}

console.log(factorial(number));
