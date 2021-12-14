// return an object on success and error object on failure
import { uploadPhoto, createUser } from './utils';

async function asyncUploadUser() {
  try {
    const upload = await uploadPhoto();
    const user = await createUser();
    const output = {
      photo: upload,
      user,
    };
    return output;
  } catch (error) {
    const output = {
      photo: null,
      user: null,
    };
    return output;
  }
}
export default asyncUploadUser;
