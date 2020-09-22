#!/usr/bin/node
if (process.argv[2]) {
  const request = require('request');
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2].toString();

  request(url, function (err, res, body) {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(body).title);
  });
}
