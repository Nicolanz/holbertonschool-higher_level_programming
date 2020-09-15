#!/usr/bin/node
function factorial (num) {
  if (isNaN(num)) {
    return (1);
  } else if (num === 0) {
    return (1);
  }
  return (num * factorial(num - 1));
}
const result = factorial(parseInt(process.argv[2]));
console.log(result);
