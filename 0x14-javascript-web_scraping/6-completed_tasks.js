#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data:', response.statusMessage);
    return;
  }

  const todos = JSON.parse(body);

  const completedTasksByUser = {};

  // Iterate over each todo item in the todos array
  todos.forEach(todo => {
    // Check if the current todo item is completed
    if (todo.completed) {
      // Check if the userId property of the current todo exists in the completedTasksByUser object
      if (!completedTasksByUser[todo.userId]) {
        // If the userId does not exist in completedTasksByUser, initialize it with 1
        completedTasksByUser[todo.userId] = 1;
      } else {
        // If the userId already exists in completedTasksByUser, increment the count of completed tasks for that user
        completedTasksByUser[todo.userId]++;
      }
    }
  });

  console.log(completedTasksByUser);
});
