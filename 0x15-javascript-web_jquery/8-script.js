$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('ul#list_movies').append(
    data.results.map((movie) => `<li>${movie.title}</li>`)
  );
});
