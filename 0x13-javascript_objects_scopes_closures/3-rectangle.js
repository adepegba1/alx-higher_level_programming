#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const row = 'X'.repeat(this.width);
      console.log(row);
    }
  }
};
