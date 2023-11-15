#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (!isNaN(num)) {
	for (let p = 0; p < num; p++) {
		console.log('C is fun');
	}
} else {
	console.log('Missing number of occurences');
}
