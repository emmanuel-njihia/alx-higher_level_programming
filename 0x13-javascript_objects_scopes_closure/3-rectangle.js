#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let k = 0; k < this.height; k++) {
      let y = '';
      for (let g = 0; g < this.width; g++) {
        y += 'X';
      }
      console.log(y);
    }
  }
}

module.exports = Rectangle;
