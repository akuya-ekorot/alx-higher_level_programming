#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();

test('check instance of 0-rectangle', () => {
  expect(r1).toBeInstanceOf(Rectangle);
});

test('check instance of constructor', () => {
  expect(r1.constructor).toBeInstanceOf(Rectangle.constructor)
})
