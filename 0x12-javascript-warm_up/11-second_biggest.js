#!/usr/bin/node
if ((!process.argv[2]) || (process.argv.length === 3)) {
  console.log(0);
} else {
  const array = [];
  for (let i = 2; i < process.argv.length; i++) {
    array.push(parseInt(process.argv[i]));
  }
  array.sort();
  console.log(array[array.length - 2]);
}
