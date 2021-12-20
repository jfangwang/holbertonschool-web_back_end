// Implement a function updateStudentGradeByCity that returns an
// array of students for a specific city with their new grade
export default function getStudentIdsSum(array, city, newGrades) {
  const grade = [];
  let temp = [];
  if (Array.isArray(newGrades) && Array.isArray(array)) {
    array.filter((student) => student.location === city).map((student) => {
      temp = newGrades.filter((grade) => grade.studentId === student.id);
      return (grade.push({ ...student, grade: temp[0] ? temp[0].grade : 'N/A' }));
    });
  }
  return (grade);
}
