#!/usr/bin/node
const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    let letter;
    if (c) {
      letter = c;
    } else {
      letter = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(letter);
      }
      console.log();
    }
  }
}
module.exports = Square;
