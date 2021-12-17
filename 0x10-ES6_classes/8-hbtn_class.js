// Implement a class named Airport
export default class Airport {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return this._size;
    if (hint === 'string') return this._location;
    return ('nothing');
  }
}
