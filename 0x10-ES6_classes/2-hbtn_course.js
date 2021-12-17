// Implement a class named HolbertonCourse
export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Length must be a number');
    if (Array.isArray(students)) throw TypeError('Students must be an array');
    students.forEach((person) => { if (typeof person !== 'string') throw TypeError('Students must be an array of strings'); });
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(nname) {
    if (typeof nname !== 'string') throw TypeError('Name must be a string');
    this._name = nname;
  }

  set length(nlength) {
    if (typeof nlength !== 'number') throw TypeError('Length must be a number');
    this._length = nlength;
  }

  set students(nstudents) {
    if (Array.isArray(nstudents)) throw TypeError('Students must be an array');
    nstudents.forEach((person) => { if (typeof person !== 'string') throw TypeError('Students must be an array of strings'); });
    this._students = nstudents;
  }
}
