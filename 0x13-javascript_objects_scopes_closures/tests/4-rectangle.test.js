#!/usr/bin/node
const Rectangle = require('../4-rectangle');

describe('Tests for 4-rectangle', () => {
  test('Rotate', () => {
    const r1 = new Rectangle(2, 3);

    expect(r1.height).toBe(3);
    expect(r1.width).toBe(2);

    r1.rotate();

    expect(r1.height).toBe(2);
    expect(r1.width).toBe(3);
  });

  test('Double', () => {
    const r2 = new Rectangle(2, 3);

    expect(r2.height).toBe(3);
    expect(r2.width).toBe(2);

    r2.double();

    expect(r2.height).toBe(6);
    expect(r2.width).toBe(4);
  });
})
