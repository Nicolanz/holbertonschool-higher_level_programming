#!/usr/bin/node
if (process.argv[2]) {
  const request = require('request');
  const url = process.argv[2].toString();

  request(url, function (err, res, body) {
    if (err) { console.log(err); }
    const list = JSON.parse(body).results;
    let counter = 0;
    for (let i = 0; i < list.length; i++) {
      if (list[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        counter++;
      }
    }
    console.log(counter);
  });
}
