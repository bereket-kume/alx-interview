#!/usr/bin/node

const request = require('request');

function fetchMovieAndCharacters(movieId) {
    const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

    request({ url: movieUrl, json: true }, (error, response, movieData) => {
        let completedRequests = 0;
        const totalRequests = movieData.characters.length;

        movieData.characters.forEach(characterUrl => {
            request({ url: characterUrl, json: true }, (error, response, characterData) => {
                if (error) {
                    console.error('Error fetching character data:', error);
                } else if (response.statusCode === 200) {
                    console.log(characterData.name);
                }
            });
        });
    });
}


movieId = process.argv[2]
fetchMovieAndCharacters(movieId);