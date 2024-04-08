#!/usr/bin/node
const fs = require('fs');

// Get file path and string to write from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurred during writing
    console.error(err);
  }
});
