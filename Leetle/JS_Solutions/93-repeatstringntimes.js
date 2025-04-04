/*
Write a function solve that repeats a string n times.

Example:
Input: ("hi", 3)
Output: "hihihi"
*/

const solve = (string, num) => {
    let str = ""
    for (let x = 0; x < num; x++) {
        str += string
    }
    return str
}

console.log(solve('hi', 3))
console.log(solve('hi ', 3))

// js one liner solution
const oneliner = (string, num) => {
    return string.repeat(num)
}

console.log(oneliner('hi', 3))
console.log(oneliner('hi ', 3))
