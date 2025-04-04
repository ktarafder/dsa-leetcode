/*
Write a function solve that finds the minimum value in a list.

Example:
Input: [3, 1, 4, 2]
Output: 1 
*/

// initial tired 1 am solution 
const solve = (arr) => {
    let minNum = Infinity
    for (num of arr) {
        if (num < minNum) {
            minNum = num
        }
    }
    return minNum
}

console.log(solve([3, 1, 4, 2]))

// realized js has a min function like python — duh 
const solve2 = (arr) => {
    minNum = Infinity
    for (num of arr) {
        minNum = Math.min(minNum, num)
    }
    return minNum
}

console.log(solve2([3, 1, 4, 2, -1]))

// one liner solution on leetle utilizing js spread operator 
const oneliner = (arr) => {
    return Math.min(...arr)
}

console.log(solve([3, 1, 4, 2]))