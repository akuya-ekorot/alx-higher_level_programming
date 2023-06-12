#!/usr/bin/node
const addMeMaybe = require('./102-call_me_maybe').addMeMaybe
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
