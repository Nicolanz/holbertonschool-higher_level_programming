#!/usr/bin/node
if (process.argv[2]) {
  const fs = require('fs');
  const buf1 = fs.readFileSync(process.argv[2]);
  const str1 = buf1.toString();
  const buf2 = fs.readFileSync(process.argv[3]);
  const str2 = buf2.toString();

  const myStr = str1.concat(str2);
  fs.writeFile(process.argv[4], myStr, function (err, file) {
    if (err) throw err;
  });
}
