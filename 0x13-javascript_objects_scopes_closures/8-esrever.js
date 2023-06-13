#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];

  for (let i = 0, j = list.length; i < list.length; i++) {
    reversed.push(list[--j]);
  }

  return reversed;
};
