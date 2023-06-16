#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);
const URLstring = 'https://swapi.dev/api/films/' + myArgs[0];

function characterFunc (filmCharacters, allCharacters, i = 0) {
  if (i === filmCharacters.length) {
    return;
  }
  const characterUrl = filmCharacters[i];
  const characterIndex = allCharacters.findIndex(c => c.url === characterUrl);
  if (characterIndex >= 0) {
    console.log(allCharacters[characterIndex].name);
  } else {
    console.log('Character not found');
  }
  characterFunc(filmCharacters, allCharacters, i + 1);
}

request(URLstring, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const filmCharacters = JSON.parse(body).characters;
    request('https://swapi.dev/api/people', function (err, response, body) {
      if (err) {
        console.log(err);
      } else {
        const allCharacters = JSON.parse(body).results;
        characterFunc(filmCharacters, allCharacters);
      }
    });
  }
});
