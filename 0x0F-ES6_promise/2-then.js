// return an object on success and error object on failure
function handleResponseFromAPI(promise) {
  return promise.then(() => ({ status: 200, body: 'success' })).catch(() => new Error()).finally(() => console.log('Got a response from the API'));
}
export default handleResponseFromAPI;
