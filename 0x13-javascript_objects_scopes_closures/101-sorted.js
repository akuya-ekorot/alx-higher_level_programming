#!/usr/bin/node

const dict = require('./101-data').dict;
const sorted = {};
const keys = Object.keys(dict);
const values = Object.values(dict);

values.forEach((value) => {
  sorted[value] = keys.filter((v) => dict[v] === value);
});

console.log(sorted);
