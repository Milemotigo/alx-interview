#!/usr/bin/node

const request = require('request');

const film_id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${film_id}/`;

function fetch_star_wars() {
    request(url, (error, response, res_body) => {
        if (error) {
            console.log(`${error}`);
        }
        let data = JSON.parse(res_body);
        let characters = data.characters
        
        for (const characterUrl of characters) {
            request(characterUrl, function(error, responseChar, responseBody) {
                if (error) {
                    console.log(`Error fetching data: ${characterUrl}`)
                }
                const JSONResponse = JSON.parse(responseBody)
                console.log(JSONResponse.name)
            });
        }
    });
}

fetch_star_wars()