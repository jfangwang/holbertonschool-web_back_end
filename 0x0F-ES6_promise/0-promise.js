// Simple get response from api in js
function getResponseFromAPI() {
  const promise = new Promise((resolve) => {
    resolve('Promise received');
  });
  return promise;
}
export default getResponseFromAPI;
