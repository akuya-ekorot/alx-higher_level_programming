#!/usr/bin/node

const logMe = require('../9-logme').logMe

describe('Tests for 9-logme', () => {
  test('First log', () => {
    logMe('Hello');

    expect(0).toBe(0);
  });
})
