#!/usr/bin/node

const request = require('request');

const film_id = process.argv[2];
url = `https://swapi-api.alx-tools.com/api/films/${film_id}/`;

function fetch_api() {
    request(url, (error, response, body) => {
        if (error){
            console.log('error');
        }
        const res_json = JSON.parse(body);
        const characters = res_json.characters;

        for (const charactersUrl of characters) {
            request(charactersUrl, (error, response, body) => {
                if (!error && response.statusCode === 200) {
                    const char_json = JSON.parse(body);
                    console.log(char_json.name);
                }
            });
        }
    });
}

fetch_api()
