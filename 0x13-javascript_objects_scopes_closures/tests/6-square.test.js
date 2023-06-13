#!/usr/bin/node

const Square = require('../6-square');

describe('Tests for 6-square', () => {
  const spy = jest.spyOn(console, "log");

  test('charPrint prints using provided character', () => {
    const s1 = new Square(4);

    s1.charPrint('c');

    expect(spy).toHaveBeenCalledWith('c'.repeat(4));
    expect(spy).toHaveBeenCalledTimes(4);
  });

  test('charPrint prints using default if character is undefined', () => {
    const s2 = new Square(4);

    s2.charPrint();

    expect(spy).toHaveBeenCalledWith('X'.repeat(4));
    expect(spy).toHaveBeenCalledTimes(4);
  })
})
