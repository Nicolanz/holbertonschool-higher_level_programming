#!/usr/bin/node
if (process.argv[2]) {
  const request = require('request');
  const url = process.argv[2].toString();
  const people = 'https://swapi-api.hbtn.io/api/people/';
  const id = 18;
  let counter = 0;

  request(url, function (err, res, body) {
    if (err) { console.log(err); }
    const list = JSON.parse(body).results;
    for (let i = 0; i < list.length; i++) {
      if (list[i].characters.includes(people + id.toString() + '/')) {
        counter++;
      }
    }
    console.log(counter);
  });
}
