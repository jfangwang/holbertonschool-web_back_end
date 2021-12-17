// Implement a class named Car
import Car from './10-car';

export default class EVCar extends Car{
  constructor(brand, motor, color, range) {
    super(brand, motor, color)
    this._range = range;
  }

  cloneCar() {
    const Obj = this.constructor;
    const clone = new Obj();
    return clone;
  }
}
