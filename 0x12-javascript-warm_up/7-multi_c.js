#!/usr/bin/node

// Get the value of x from the command-line argument
const x = process.argv[2];

// Check if x is a valid number
if (x === undefined || isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  // Convert x to an integer
  const numOccurrences = parseInt(x);
  let i = 0;
  while (i < numOccurrences) {
    console.log('C is fun');
    i++;
  }
}
