#!/usr/bin/node
let i;
const size = parseInt(process.argv[2], 10);

if (process.argv[2] && isNaN(size) === false) {
  for (i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
