#!/usr/bin/node
let call = 0;
exports.logMe = function (str) {
  console.log(call + ': ' + str);
  call++;
};
