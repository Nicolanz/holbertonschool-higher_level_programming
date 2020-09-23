#!/usr/bin/node
if (process.argv[2]){
    const request = require('request');
    const fs = require('fs');

    request(process.argv[2], function (err, res, body) {
        fs.writeFile(process.argv[3], body, 'utf-8', function (err, file) {
            if (err) {
                console.log(err);
            }
        });
    });
}
