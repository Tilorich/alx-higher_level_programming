#!/usr/bin/node
const info = process.argv[2];
if (isNaN(info) || info === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(info); i++) {
    let row = '';
    for (let j = 0; j < parseInt(info); j++) {
      row += 'X';
    }
    console.log(row);
  }
}
