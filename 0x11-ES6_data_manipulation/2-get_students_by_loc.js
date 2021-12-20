// Implement a function getStudentsByLocation
export default function getStudentsByLocation(array, city) {
  let output = [];
  if (Array.isArray(array)) {
    output = array.filter((item) => item.location === city);
  }
  return output;
}
