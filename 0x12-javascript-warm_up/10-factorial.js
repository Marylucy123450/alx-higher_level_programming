#!/usr/bin/node

function factorial (n) {
  // Base case: factorial of 0 or 1 is 1
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  // Recursive case: compute factorial using recursion
  return n * factorial(n - 1);
}

// Get the integer from command-line argument
const num = parseInt(process.argv[2]);

// Compute factorial and print the result
console.log(factorial(num));
