// return an object on success and error object on failure
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((results) => {
      const output = {};
      let temp = {};
      results.forEach((result) => {
        if (result.status === 'fulfilled') {
          output.push(result);
        } else {
          temp = {
            status: result.status,
            value: result.value,
          };
          output.push(temp);
        }
      });
      return output;
    })
    .catch(() => {});
}
export default handleProfileSignup;
