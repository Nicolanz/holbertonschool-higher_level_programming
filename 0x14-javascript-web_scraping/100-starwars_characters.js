#!/usr/bin/node
if (process.argv[2]) {
  const request = require('request');
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2].toString();

  request(url, (err, res, body) => {
    if (err) { console.log(err); }
    const charList = JSON.parse(body).characters;
    let i = 0;
    for (i in charList) {
      request(charList[i], (error, response, body1) => {
        if (error) { console.log(error); }
        console.log(JSON.parse(body1).name);
      });
    }
  });
}
