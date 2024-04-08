#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // Create an empty object if width or height is not a positive integer or equal to 0
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // Swap the width and height values
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Double the width and height values
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
