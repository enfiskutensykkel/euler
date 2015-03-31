#!/usr/bin/env nodejs
// Algorithm taken from http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

function periods(S) {
	var m = 0;
	var d = 1;
	var a = Math.floor(Math.sqrt(S));
	var a0 = a;

	var set = []; // keep track of when the iterations start looping
	var n;

	for (n = 0; !set[[m, d, a]]; ++n) {
		set[[m, d, a]] = true;
		
		m = d * a - m;
		d = (S - m * m) / d;
		a =	Math.floor((a0 + m) / d);
	}
	n -= 1;

	return n;
}


var odds = 0;
for (var i = 2; i <= 10000; ++i) {
	
	// Avoid perfect squares
	var root = Math.sqrt(i);
	if (root != Math.floor(root))
		if (periods(i) & 1) // we're only interested in odd periods
			++odds;
}

console.log(odds);
