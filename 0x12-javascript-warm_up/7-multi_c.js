#!/usr/bin/node
let i;
if (process.argv[2]) {
  const num = parseInt(process.argv[2]);
  if (isNaN(num)) {
    console.log('Missing number of occurrences');
  } else {
    for (i = 0; i < num; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
