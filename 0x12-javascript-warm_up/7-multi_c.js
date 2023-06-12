#!/usr/bin/node

let iter = process.argv[2];

if (!iter) {
  console.log('Missing number of occurrences');
} else {
  while (iter-- && iter > 0) {
    console.log('C is fun');
  }
}
