#!/usr/bin/node

const fs = require('fs');
const [Path1, Path2, dest] = process.argv.splice(2);

const file1 = fs.readFileSync(Path1, 'utf8');
const file2 = fs.readFileSync(Path2, 'utf8');

const concated = file1 + file2;

fs.writeFileSync(dest, concated, 'utf8');
