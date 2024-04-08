#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

// Get the two integers from command-line arguments
const num1 = process.argv[2];
const num2 = process.argv[3];

// Print the addition of the two integers
console.log(add(num1, num2));
