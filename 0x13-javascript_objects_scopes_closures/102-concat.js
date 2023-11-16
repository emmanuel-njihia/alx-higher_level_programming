#!/usr/bin/node
const fsf = require('fs');

const firstArg = fsf.readFileSync(process.argv[2]).toString();
const secondArg = fsf.readFileSync(process.argv[3]).toString();
fsf.writeFileSync(process.argv[4], firstArg + secondArg);
