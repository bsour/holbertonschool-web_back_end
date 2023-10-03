import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ];

  const results = [];

  for (const promise of promises) {
    try {
      const value = await promise;
      results.push({ status: 'fulfilled', value });
    } catch (error) {
      results.push({ status: 'rejected', value: error });
    }
  }

  return results;
}

export default handleProfileSignup;
