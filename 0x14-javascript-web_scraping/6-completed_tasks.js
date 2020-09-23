#!/usr/bin/node
if (process.argv[2]) {
  const request = require('request');

  request(process.argv[2], function (err, res, body) {
    if (err) { console.log(err); } else {
      const users = JSON.parse(body);
      const dict = {};
      let tasks = 0;

      for (let i = 0; i < users.length; i++) {
        if (users[i].completed === true) {
          tasks++;
        }
        if (!users[i + 1]) {
          dict[users[i].userId] = tasks;
          break;
        }
        if (users[i + 1].userId > users[i].userId) {
          dict[users[i].userId] = tasks;
          tasks = 0;
        }
      }
      console.log(dict);
    }
  });
}
