#!/usr/bin/node

try {
  const number = parseInt(process.argv[2]);

  if (number) {
    console.log('My number:', number);
  } else {
    throw new Error();
  }
} catch (e) {
  console.log('Not a number');
}
