let notes1 = `939
7,13,x,x,59,x,31,19`;

let notes2 = `1000303
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,541,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,983,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19`;

let schedule = notes2.split("\n");
let timestamp = parseInt(schedule[0]);
let buses = schedule[1].split(",").filter(x=>parseInt(x)).map(x=>parseInt(x))

let num = timestamp-(timestamp%buses[0])+buses[0];
let currIndex = 0;
function earlyBus(buses) {
	for (let i=0; i<buses.length; i++) {
		if (num>timestamp-(timestamp%buses[i])+buses[i]) {
			num = timestamp-(timestamp%buses[i])+buses[i];
			currIndex = i;
		}
	} return buses[currIndex]*(num-timestamp)
}

// console.log(earlyBus(buses))

// part 2 --------------------------------------------



// not working



// inclues "x"
let allBuses = schedule[1].split(",");
// console.log(allBuses);
// doesn't include "x"
// console.log(buses);

let remainders = [0];
function getRemainders(buses) {
	for (let i=1; i<buses.length; i++) {
			if (buses[i]!="x") {
				if (buses[i]>=i) {
					remainders.push(parseInt(buses[i])-i);
					// console.log(buses[i], i)
				} 
				else {
					// console.log(i, buses[i]);
					let num = i;
					// console.log(num, buses[i]);
					while (num>buses[i]) {
						num -= parseInt(buses[i]);
					}
					console.log(num, buses[i], i)
					remainders.push(num)
				}
			}
		} 
}
getRemainders(allBuses);
console.log(remainders);

let product = buses.reduce((a,b)=>a*b,1);
// console.log(product);

// array of (product/each number)
let pp = [];
function getpp(buses, product) {
	for (let i=0; i<buses.length; i++) {
		pp.push(product/buses[i]);
	}
}
getpp(buses, product);
// console.log(pp);

// taken from net because I do not understand this much math, this calculates modular multiplicative inverse of a wrt m
function modinv(a,m) {
    var v = 1;
    var d = a;
    var u = (a == 1);
    var t = 1-u;
    if (t == 1) {
        var c = m % a;
        u = Math.floor(m/a);
        while (c != 1 && t == 1) {
               var q = Math.floor(d/c);
               d = d % c;
               v = v + q*u;
               t = (d != 1);
               if (t == 1) {
                   q = Math.floor(c/d);
                   c = c % d;
                   u = u + q*v;
               }
        }
        u = v*(1 - t) + t*(m - u);
    }
    return u;
}

let inv = [];
function getInverse(pp, numbers) {
	for (let i=0; i<pp.length; i++) {
		inv.push(modinv(pp[i], numbers[i]));
	}
}

getInverse(pp, buses);
// console.log(inv);

function getTimestamp(buses) {
	let timestamp = 0;
	for (let i=0; i<buses.length; i++) {
		timestamp += (remainders[i]*pp[i]*inv[i]);
		// console.log(timestamp);
	}
	return timestamp%product;
}

console.log(getTimestamp(buses))
