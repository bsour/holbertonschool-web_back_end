import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ];

  const results = await Promise.all(promises);

  return results.map((result) => ({
    status: result instanceof Error ? 'rejected' : 'fulfilled',
    value: result instanceof Error ? result.message : result,
  }));
}
