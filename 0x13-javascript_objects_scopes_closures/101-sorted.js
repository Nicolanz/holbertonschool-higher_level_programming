#!/usr/bin/node
const firstDict = require('./101-data').dict;
const newList = [];
const newDict = {};
let i = 0;
for (const key in firstDict) {
  if (!newList.includes(firstDict[key])) {
    const otherList = [];
    newList.push(firstDict[key]);
    for (const otherKey in firstDict) {
      if (firstDict[otherKey] === newList[i]) {
        otherList.push(otherKey);
      }
    }
    i++;
    newDict[firstDict[key]] = otherList;
  }
}
console.log(newDict);
