#!/usr/bin/node

const args = process.argv;

function getSeconBiggest (args) {
  if (args.length <= 3) {
    return 0;
  }

  let largest;
  let second = 0;
  const list = args.splice(2);

  list.forEach((number, idx) => {
    number = parseInt(number);

    if (idx === 0) {
      largest = number;
    }

    if (number > largest) {
      second = largest;
      largest = number;
    }

    if (number < largest && number > second) {
      second = number;
    }
  });

  return second;
}

console.log(getSeconBiggest(args));
