#!/usr/bin/node
const firstArgs = process.argv.length;
if (firstArgs > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
