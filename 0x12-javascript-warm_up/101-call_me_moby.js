#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
	for (let p = 0; p < x; p++) theFunction();
};
