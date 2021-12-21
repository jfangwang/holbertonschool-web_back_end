// Implement a function getListStudentIds that returns an array of ids from a list of object
export default function getListStudentIds(array) {
  if (Array.isArray(array)) {
    return array.map((item) => item.id);
  }
  return ([]);
}
