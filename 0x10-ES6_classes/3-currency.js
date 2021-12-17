// Implement a class named Currency
export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
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
