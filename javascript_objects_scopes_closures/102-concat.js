#!/usr/bin/node

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');
let textA = fs.readFileSync(fileA, 'utf8');
let textB = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, textA + textB);
