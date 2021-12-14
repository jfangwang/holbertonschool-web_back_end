// return an object on success and error object on failure
import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((messages) => {
    }
}
export default handleProfileSignup;
