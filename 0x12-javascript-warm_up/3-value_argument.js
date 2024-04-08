#!/usr/bin/node

// Check if an argument was passed
if (process.argv[2] === undefined) {
  // If no argument was passed, print "No argument"
  console.log('No argument');
} else {
  // If an argument was passed, print the value of the first argument
  console.log(process.argv[2]);
}
