// return an object on success and error object on failure
function signUpUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}
export default signUpUser;
