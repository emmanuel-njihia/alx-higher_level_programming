#!/usr/bin/node
const { argv } = require('process');

if (isNaN(Number(argv[2]))) {
  console.log('Missing size');
} else {
  let i = 1;
  const x = argv[2];
  for (i; i <= x; i++) {
    let j = 1;
    while (j <= x) {
      process.stdout.write('X');
      j++;
    }
    console.log();
  }
}
