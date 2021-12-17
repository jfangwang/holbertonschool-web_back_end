// Implement a class named Car
export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const Species = this.constructor;
    const clone = new Species(this._brand, this._motor, this._color);
    return clone;
  }
}
