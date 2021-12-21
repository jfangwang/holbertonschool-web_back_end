// Implement a function getStudentIdsSum
export default function getStudentIdsSum(array) {
  if (Array.isArray(array)) {
    return (array.reduce((sum, item) => sum + item.id, 0));
  }
  return (0);
}
