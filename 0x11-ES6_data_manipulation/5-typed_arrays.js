// Implement a function createInt8TypedArray that returns a new ArrayBuffer with
// an Int8 value at a specific position.
export default function createInt8TypedArray(length, position, value) {
  const arrBuff = new ArrayBuffer(length);
  const view = new DataView(arrBuff, 0);

  if (position >= length) {
    throw Error('Position outside range');
  } else {
    view.setInt8(position, value);
  }
  return (view);
}
