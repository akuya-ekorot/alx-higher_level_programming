#!/usr/bin/node
const Rectangle = require('../3-rectangle')

test('Prints 3 rows, 2 cols', () => {
  const spy = jest.spyOn(console, 'log');
  const r1 = new Rectangle(2, 3);
  r1.print();

  expect(spy).toHaveBeenCalledWith('X'.repeat(2));
  expect(spy).toHaveBeenCalledTimes(3);
});

test('Prints 5 rows, 10 cols', () => {
  const spy = jest.spyOn(console, 'log');
  const r2 = new Rectangle(10, 5);
  r2.print();

  expect(spy).toHaveBeenCalledWith('X'.repeat(10));
  expect(spy).toHaveBeenCalledTimes(8);
})
