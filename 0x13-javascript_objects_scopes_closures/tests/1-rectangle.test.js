#!/usr/bin/node
const Rectangle = require('../1-rectangle')

describe('Tests for 1-rectangle', () => {
  test('Initialize Rectangle with width 2, height 3', () => {
    const r1 = new Rectangle(2, 3);
    expect(r1).toBeInstanceOf(Rectangle);
    expect(r1.width).toBe(2);
    expect(r1.height).toBe(3);
  });

  test('Initialize Rectangle with width 2, height -3', () => {
    const r1 = new Rectangle(2, -3);
    expect(r1).toBeInstanceOf(Rectangle);
    expect(r1.width).toBe(2);
    expect(r1.height).toBe(-3);
  });

  test('Initialize Rectangle with width 2', () => {
    const r1 = new Rectangle(2);
    expect(r1).toBeInstanceOf(Rectangle);
    expect(r1.width).toBe(2);
    expect(r1.height).toBe(undefined);
  });
})
