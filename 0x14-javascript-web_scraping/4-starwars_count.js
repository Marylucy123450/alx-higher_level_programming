#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve data. Status code:', response.statusCode);
    return;
  }

  const films = JSON.parse(body).results;
  const wedgeAntillesMovies = films.filter(film =>
    film.characters.some(character => character.includes('/18/'))
  );

  console.log(wedgeAntillesMovies.length);
});
