#!/usr/bin/node

// Get the command-line arguments excluding the first two
// (which are the script interpreter and filename)
const args = process.argv.slice(2);

// If no arguments or only one argument is provided, print 0 and exit
if (args.length <= 1) {
  console.log(0);
  process.exit(0);
}

// Convert arguments to integers and sort them in ascending order
const numbers = args.map(Number).sort((a, b) => a - b);

// Print the second largest number
console.log(numbers[numbers.length - 2]);
