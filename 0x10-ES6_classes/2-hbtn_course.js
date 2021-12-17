// Implement a class named HolbertonCourse
export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() { return this._name; }

  get length() { return this._length; }

  get students() { return this._students; }

  set name(nname) {
    if (typeof nname !== 'string') throw TypeError('name must be a string');
    this._name = nname;
  }

  set length(nlength) {
    if (typeof nlength !== 'number') throw TypeError('length must be a number');
    this._length = nlength;
  }

  set students(nstudents) {
    if (Array.isArray(nstudents)) throw TypeError('students must be an array');
    nstudents.forEach((person) => { if (typeof person !== 'string') throw TypeError('students must be an array of strings'); });
    this._students = nstudents;
  }
}
