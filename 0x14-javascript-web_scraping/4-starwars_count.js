#!/usr/bin/node
if (process.argv[2]) {
  const request = require('request');
  const url = 'https://swapi-api.hbtn.io/api/people/18/';
  const api = 'https://swapi-api.hbtn.io/api/films/';

  let pam = process.argv[2].toString();
  if (pam[pam.length] !== '/') {
    pam = pam + '/';
  }

  if (pam === api) {
    request(url, function (err, res, body) {
      if (err) { console.log(err); }
      console.log((JSON.parse(body).films.length));
    });
  }
}
