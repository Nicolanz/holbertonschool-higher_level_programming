#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv.length === 3) {
  console.log(0);
} else {
  const array = [];
  for (let i = 2; i < process.argv.length; i++) {
    array.push(parseInt(process.argv[i]));
  }
  const max = Math.max.apply(null, array);
  array.splice(max);
  array.splice(array.indexOf(max), 1);
  console.log(Math.max.apply(null, array));
}
