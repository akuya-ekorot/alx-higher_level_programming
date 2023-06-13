#!/usr/bin/node
const Rectangle = require('../0-rectangle');

const r1 = new Rectangle();

test('check instance of 0-rectangle', () => {
  console.log(r1);
  expect(r1).toBeInstanceOf(Rectangle);
});

test('check instance of constructor', () => {
  console.log(r1.constructor);
  expect(r1.constructor).toBeInstanceOf(Rectangle.constructor)
})
