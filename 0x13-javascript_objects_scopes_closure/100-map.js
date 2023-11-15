#!/usr/bin/node
const listOne = require('./100-data').list;
const ListTwo = list.map(function (number, index) {
  return number * index;
});

console.log(listOne);
console.log(ListTwo);
