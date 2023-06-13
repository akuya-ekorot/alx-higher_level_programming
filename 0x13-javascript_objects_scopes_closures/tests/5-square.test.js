#!/usr/bin/node

const Square = require('../5-square');
const Rectangle = require('../4-rectangle');

describe('Tests for 5-square', () => {
  test('Initializing a square', () => {
    const s1 = new Square(4);

    expect(s1).toBeInstanceOf(Square);
    expect(s1).toBeInstanceOf(Rectangle);
    expect(s1.height).toBe(s1.width);
  });

  test('Square can print', () => {
    const spy = jest.spyOn(console, "log");
    const s2 = new Square(4);

    s2.print();

    expect(spy).toHaveBeenCalledWith('X'.repeat(4));
    expect(spy).toHaveBeenCalledTimes(4);
  });

  test('Double method works', () => {
    const s3 = new Square(4);

    s3.double();

    expect(s3.height).toBe(8);
    expect(s3.width).toBe(8);
  });
})
