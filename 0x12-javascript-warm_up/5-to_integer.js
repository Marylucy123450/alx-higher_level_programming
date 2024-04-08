#!/usr/bin/node

// Get the first argument from the command line
const arg = process.argv[2];

// Convert the argument to an integer using parseInt()
const num = parseInt(arg);

// Check if the conversion resulted in a valid integer
if (!isNaN(num)) {
  // If it's a valid integer, print "My number: <integer>"
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
