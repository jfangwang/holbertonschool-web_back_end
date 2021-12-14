// return an object on success and error object on failure
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((data) => {
      const output = [];
      for (let i = 0; i < data.length; i += 1) {
        if (data[i].status === 'fulfilled') {
          output.push(data[i]);
        } else {
          output.push({
            status: data[i].status,
            value: `Error: ${data[i].reason}`,
          });
        }
      }
      return output;
    });
}
export default handleProfileSignup;
