// Implement a function setFromArray that returns a Set from an array.
export default function setFromArray(array) {
  let output = [];
  if (Array.isArray(array)) {
    output = new Set(array);
  }
  return (output);
}
