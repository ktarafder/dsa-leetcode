/*
Write a function solve that checks if all elements in a list are unique (no duplicates).

Example:
Input: [1, 2, 3, 4]
Output: True
*/

const solve = (arr) => {
    let set = new Set();
    for (let index = 0; index < arr.length; index++) {
        if (set.has(arr[index])) {
            return false
        }
        set.add(arr[index])
    }
    return true
}

console.log(solve([1,2,3,4]))
console.log(solve([1,2,1,4]))

// We can rewrite the for loop like this using the for ... of, so we don't have to handle index manually
const solve2 = (arr) => {
    let set = new Set();
    for (const num of arr) {
        if (set.has(num)) return false;
        set.add(num);
    }
    return true;
};

console.log(solve2([1,2,3,4]))
console.log(solve2([1,2,1,4]))