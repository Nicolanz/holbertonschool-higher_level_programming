#!/usr/bin/node
const firstList = require('./100-data').list;
let i = 0;
const secondList = firstList.map(x => x * i++);
console.log(firstList);
console.log(secondList);
