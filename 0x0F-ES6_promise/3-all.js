// return an object on success and error object on failure
import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((data) => { console.log(data[0].body + ' ' + data[1].firstName + ' ' + data[1].lastName) });
}
export default handleProfileSignup;
