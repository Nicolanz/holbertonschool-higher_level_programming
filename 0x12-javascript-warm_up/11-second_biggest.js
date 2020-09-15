#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log(0);
} else {
  const array = [];
  for (let i = 2; i < process.argv.length; i++) {
    array.push(parseInt(process.argv[i]));
  }
  if (array.length === 1) {
    console.log(0);
  } else {
    array.sort();
    console.log(array[array.length - 2]);
  }
}
