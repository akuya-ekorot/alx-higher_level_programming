#!/usr/bin/node

const nbOccurences = require('../7-occurrences').nbOccurences;

describe('Tests for 7-occurrences', () => {
  test('one occurrence', () => {
    expect(nbOccurences([1, 2, 3, 4, 5, 6], 3)).toBe(1);
  });

  test('4 occurrences', () => {
    expect(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3)).toBe(4);
  });

  test('2 occurrences', () => {
    expect(nbOccurences(["S", 12, "c", "S", "School", 8], "S")).toBe(2);
  });

  test('no occurrences', () => {
    expect(nbOccurences(["S", 12, "c", "S", "School", 8], 3)).toBe(0);
  });
})
