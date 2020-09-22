#!/usr/bin/node
if (process.argv[2]) {
  const request = require('request');
  request(process.argv[2], function (response) {
    console.log('code: ' + response.statusCode);
  });
}
