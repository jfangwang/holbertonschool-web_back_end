// Implement a function getStudentIdsSum
export default function getStudentIdsSum(array) {
  let count = 0;
  if (Array.isArray(array)) {
    array.forEach((item) => {
      count += item.id;
    });
  }
  return (count);
}
