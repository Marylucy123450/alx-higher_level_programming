#!/usr/bin/node

// Get the size of the square from the command-line argument
const size = process.argv[2];

// Check if size is a valid number
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // Convert size to an integer
  const squareSize = parseInt(size);

  // Check if squareSize is positive
  if (squareSize > 0) {
    // Loop to print the square
    for (let i = 0; i < squareSize; i++) {
      // Print a row of 'X's
      console.log('X'.repeat(squareSize));
    }
  } else {
    console.log('Missing size');
  }
}
