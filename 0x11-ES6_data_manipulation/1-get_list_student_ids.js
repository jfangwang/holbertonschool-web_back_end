// Implement a function getListStudentIds that returns an array of ids from a list of object
export default function getListStudentIds(array) {
  const output = [];
  if (Array.isArray(array)) {
    array.forEach((item) => {
      output.push(item.id);
    });
  }
  return output;
}
