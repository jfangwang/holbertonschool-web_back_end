// Implement a class named Currency
export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') throw TypeError('code must be a string');
    if (typeof name !== 'string') throw TypeError('name must be a number');
    this._code = code;
    this._name = name;
  }

  displayFullCurrency() {
    return `${name} (${code})`;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(nCode) {
    this._code = nCode;
  }

  set name(nName) {
    this._name = nName;
  }
}
