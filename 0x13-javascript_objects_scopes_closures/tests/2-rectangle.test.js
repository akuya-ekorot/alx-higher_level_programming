#!/usr/bin/node
const Rectangle = require('../2-rectangle')

describe('Tests for 2-rectangle', () => {
  test('Initialize Rectangle with width 2, height 3', () => {
    const r1 = new Rectangle(2, 3);
    expect(r1).toBeInstanceOf(Rectangle);
    expect(r1.width).toBe(2);
    expect(r1.height).toBe(3);
  });

  test('Initialize Rectangle with width 2, height -3', () => {
    const r2 = new Rectangle(2, -3);
    expect(r2).toBeInstanceOf(Rectangle);
    expect(r2.width).toBe(undefined);
    expect(r2.height).toBe(undefined);
  });

  test('Initialize Rectangle with width 2, no height', () => {
    const r3 = new Rectangle(2);
    expect(r3).toBeInstanceOf(Rectangle);
    expect(r3.width).toBe(undefined);
    expect(r3.height).toBe(undefined);
  });

  test('Initialize Rectangle with width 2, height 0', () => {
    const r4 = new Rectangle(2, 0);
    expect(r4).toBeInstanceOf(Rectangle);
    expect(r4.width).toBe(undefined);
    expect(r4.height).toBe(undefined);
  });
})
