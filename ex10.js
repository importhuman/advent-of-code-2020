// example data
let data1 = `16
10
15
5
1
11
7
19
6
12
4`;

// example 2
let data2 = `28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3`

// my input data
let data3 = `118
14
98
154
71
127
38
50
36
132
66
121
65
26
119
46
2
140
95
133
15
40
32
137
45
155
156
97
145
44
153
96
104
58
149
75
72
57
76
56
143
11
138
37
9
82
62
17
88
33
5
10
134
114
23
111
81
21
103
126
18
8
43
108
120
16
146
110
144
124
67
79
59
89
87
131
80
139
31
115
107
53
68
130
101
22
125
83
92
30
39
102
47
109
152
1
29
86`;

// convert string input to array ofsorted integers
let adapters = data3.split("\n").sort((a,b)=> a-b).map(x=>parseInt(x));
// console.log(adapters)
let adaptersUsed = [0];
for (let i=0; i<adapters.length; i++) {
	if (adapters[i]-adaptersUsed[adaptersUsed.length-1]<=3) {
		adaptersUsed.push(adapters[i]);
	}  
} 

// add device built-in adapter to adaptersUsed
adaptersUsed.push(adaptersUsed[adaptersUsed.length-1]+3);
console.log(adaptersUsed)

// to calculate solution of part 1: 
// let differences = [];
// for (let i=1; i<adaptersUsed.length; i++) {
// 	differences.push(adaptersUsed[i]-adaptersUsed[i-1]);
// }

// let counts = {};
// differences.forEach((x)=> {counts[x] = (counts[x] || 0) + 1});
// // console.log(counts[1]*counts[3])


// part 2 -----------------------------------------


let paths = adaptersUsed.map((x)=> 0);
paths[0] = 1;
// console.log(paths)
function getArrangements(list) {
	for (let i=0; i<list.length; i++) {
		for (let x=1; x<4; x++) {
			if (list.indexOf(list[i]+x)>-1) {
				let index = list.indexOf(list[i]+x);
				paths[index] += paths[i];
			}
		}
	} console.log(paths[paths.length-1])
}

getArrangements(adaptersUsed)


// why this works (taken from the subreddit) ------------------------------------------

//   -all items in the list start with 0 paths leading to them

//   -the first item in the list starts with 1 path leading to it

//   -loop throught the items and evey item adds its number of paths to all the items it can reach

// Maybe it will be easier with an example : 0, 1, 3, 4

// Start

// i   paths
// 0   1
// 1   0
// 3   0
// 4   0

// i0 : i1 + 1, i3 + 1

// i   paths
// 0   1
// 1   1
// 3   1
// 4   0

// i1 : i3 + 1, i4 + 1

// i   paths
// 0   1
// 1   1
// 3   2
// 4   1

// i3 : i4 + 2

// i   paths
// 0   1
// 1   1
// 3   2
// 4   3

// Answer is 3.