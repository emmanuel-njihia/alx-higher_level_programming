#!/usr/bin/node
exports.esrever = function (list) {
  let abc = list.length - 1;
  let k = 0;
  while ((abc - k) > 0) {
    const ax = list[abc];
    list[abc] = list[k];
    list[k] = ax;
    k++;
    abc--;
  }
  return list;
};
