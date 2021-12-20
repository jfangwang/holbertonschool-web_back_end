// Implement a function cleanSet that returns a string of all the set
// values that start with a specific string (startString)
export default function cleanSet(set, startString) {
  let output = '';
  set.forEach((word) => {
    if (word.startsWith(startString)) {
      output += `${word.substring(startString.length)}-`;
    }
  });
  output = output.substring(0, output.length - 1);
  if (startString === '') {
    output = '';
  }
  return (output);
}
