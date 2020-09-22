#!/usr/bin/node
if (process.argv[2]) {
  const request = require('request');

  request(process.argv[2], function (err, response) {
    if (err) {
      console.log(err);
    }
    console.log('code: ' + response.statusCode);
  });
}
