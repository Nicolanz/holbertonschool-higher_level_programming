#!/usr/bin/node
if (process.argv[2]) {
  const fs = require('fs');
  fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err, file) {
    if (err) {
      console.log(err);
    }
  });
}
