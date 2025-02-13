#!/usr/bin/node
// A script that reads and prints the content of a file

const request = require('request');
const fs = require('fs');
const fileLocation = process.argv[3];
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.error(err);
  fs.writeFile(fileLocation, body, err => {
    if (err) console.error(err);
  });
});
