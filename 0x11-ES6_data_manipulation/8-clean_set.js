// Implement a function cleanSet that returns a string of all the set
// values that start with a specific string (startString)
export default function cleanSet(set, startString) {
  let output = '';
  if (startString === '' || startString.length === 0) {
    return (output);
  }
  set.forEach((word) => {
    if (word && word.startsWith(startString)) {
      output += `${word.substring(startString.length)}-`;
    }
  });
  if (output.length === 0) {
    return (output);
  }
  output = output.substring(0, output.length - 1);
  return (output);
}
