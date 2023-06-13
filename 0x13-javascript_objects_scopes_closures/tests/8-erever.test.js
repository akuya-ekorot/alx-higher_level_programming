#!/usr/bin/node

const esrever = require('../8-esrever').esrever;

describe('Tests for 8-esrever', () => {
  test('check reversed', () => {
    expect(esrever([1, 2, 3, 4, 5])).toStrictEqual([5, 4, 3, 2, 1]);
  });

  test('check reversed', () => {
    expect(esrever(['String', { id: 12 }, 89, 'School']))
      .toStrictEqual(['School', 89, { id: 12 }, 'String']);
  });
});
