#!/usr/bin/node
const request = require('request');

// Get URL from command line arguments
const url = process.argv[2];

// Make a GET request to the URL
request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
