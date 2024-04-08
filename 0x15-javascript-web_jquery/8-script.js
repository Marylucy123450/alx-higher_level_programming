$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
  $('ul#list_movies').append(...response.results.map(movie => `<li>${movie.title}</li>`));
});
