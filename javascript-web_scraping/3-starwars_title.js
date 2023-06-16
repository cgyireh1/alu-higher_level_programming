#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);
const URLstring = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
request(URLstring, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
