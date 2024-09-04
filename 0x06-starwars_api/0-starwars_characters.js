#!/usr/bin/node

const request = require('request');

function fetchMovieAndCharacters (movieId) {
  const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

  request({ url: movieUrl, json: true }, (error, response, movieData) => {
    if (error) {
      console.error('Error fetching movie data:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
      return;
    }

    if (!movieData || !movieData.characters || movieData.characters.length === 0) {
      console.error('No characters found for this movie.');
      return;
    }

    movieData.characters.forEach(characterUrl => {
      request({ url: characterUrl, json: true }, (error, response, characterData) => {
        if (error) {
          console.error('Error fetching character data:', error);
        } else if (response.statusCode === 200) {
          console.log(characterData.name);
        } else {
          console.error(`Failed to fetch character data. Status code: ${response.statusCode}`);
        }
      });
    });
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

fetchMovieAndCharacters(movieId);
