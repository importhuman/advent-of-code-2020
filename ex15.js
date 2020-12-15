let start1 = [0,3,6];

let start2 = [12,20,0,6,1,17,7];

function getAllIndexes(arr, val) {
    var indexes = [], i;
    for(i = 0; i < arr.length; i++)
        if (arr[i] == val)
            indexes.push(i);
    return indexes;
}

function initialCounts(arr) {
	let counts = {};
	for (let i=0; i<arr.length; i++) {
		let num = arr[i];
		counts[num] = counts[num] ? counts[num]+1 : 1;
	} return counts;
}

// maxLength = the number in the game to get
function memoryGameArray(arr, maxLength) {
	let counts = initialCounts(arr);
	let currLength = arr.length;
	for (let i=currLength-1; i<maxLength-1; i++) {
		let lastNum = arr[i];
		if (counts[lastNum]==1) {
			arr.push(0);
		} else {
			indexes = getAllIndexes(arr, lastNum)
			arr.push(indexes[indexes.length-1]-indexes[indexes.length-2]);
		}
		counts = initialCounts(arr);
	}
	return arr[arr.length-1];
}

// console.log(memoryGameArray(start1, 2020))

// part 2 ---------------------------------------

function betterMemoryGame(arr, maxLength) {
	let lastIndexes = new Map(arr.map(num=> [num, arr.indexOf(num)]));
	let lastNum = arr[arr.length-1];
	let i = arr.length-1;
	while (i<maxLength-1){
		if (!lastIndexes.has(lastNum)) {
			lastIndexes.set(lastNum, i);
			lastNum = 0;
		}
		else {
			diff = i - lastIndexes.get(lastNum);
			lastIndexes.set(lastNum, i);
			lastNum = diff;
		}
		i++;
	}
	return lastNum;
}

console.log(betterMemoryGame(start2, 30000000))


