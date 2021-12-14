// return an object on success and error object on failure
export default function uploadPhoto(filename) {
  return Promise.reject(Error(`${filename} cannot be processed`));
}
