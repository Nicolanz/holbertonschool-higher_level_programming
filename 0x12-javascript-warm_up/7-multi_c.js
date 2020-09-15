#!/usr/bin/node
let i;
const x = parseInt(process.argv[2]);

if (process.argv[2] && isNaN(x) === false) {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
