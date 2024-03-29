#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) throw err;

  const tasks = JSON.parse(body);

  const completed = {};

  for (const task of tasks) {
    if (task.completed === true) {
      if (completed[task.userId] === undefined) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId] += 1;
      }
    }
  }
  console.log(completed);
});
