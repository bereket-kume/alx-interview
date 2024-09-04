const request = require('request');
const rp = require('request-promise');

async function fetchMovieAndCharacters(movieId) {
    try {
        // Fetch the main movie data
        const movieUrl = `https://swapi.dev/api/films/${movieId}/`;
        const movieResponse = await rp({ uri: movieUrl, json: true });
        
        // Log the movie title
        console.log(`Movie: ${movieResponse.title}`);
        
        // Loop through the character URLs and fetch each one
        for (const characterUrl of movieResponse.characters) {
            const characterResponse = await rp({ uri: characterUrl, json: true });
            console.log(`Character: ${characterResponse.name}`);
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

movieId = process.argv[2]
fetchMovieAndCharacters(movieId);
