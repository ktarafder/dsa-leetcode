/*
Write a function solve that removes duplicates from a list while preserving the original order.

Example:
Input: [1, 2, 2, 3, 4, 4]
Output: [1, 2, 3, 4] 
*/

function solve(arr) {
    const seen = new Set();
    const result = [];

    for (const i of arr) {
        if (!seen.has(i)) {
            seen.add(i);
            result.push(i);
        }
    }
    return result;
}

// One-liner solution
const solveOneLiner = arr => [...new Set(arr)];
// Explanation:
// The one-liner uses the Set object to store unique values from the array.
// The spread operator (...) is used to convert the Set back into an array.
// The Set automatically handles duplicates, so only unique values are kept.

function solve2(arr) {
    return [... new Set(arr)]
}

// Test cases
console.log(solve([1, 2, 2, 3, 4, 4])); // Output: [1, 2, 3, 4]
console.log(solve([1, 1, 1, 1])); // Output: [1]

console.log(solveOneLiner([1, 2, 2, 3, 4, 4])); // Output: [1, 2, 3, 4]
console.log(solveOneLiner([1, 1, 1, 1])); // Output: [1]

console.log(solve2([1, 2, 2, 3, 4, 4])); // Output: [1, 2, 3, 4]
console.log(solve2([1, 1, 1, 1])); // Output: [1]
