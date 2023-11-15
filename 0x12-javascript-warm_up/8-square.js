#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
	if (size > 0) {
		for (let p = 0; p < size; p++) {
			let line = '';
			for (let q = 0; q < size; q++) {
				line += 'X';
			}
			console.log(line);
		}
	} else {
		console.log('Size must be a positive integer');
	}
} else {
	console.log('Size must be a positive integer');
}
} else {
	console.log('Missing size');
}
