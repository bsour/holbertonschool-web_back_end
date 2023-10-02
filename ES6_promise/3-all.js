import { uploadPhoto, createUser } from './utils';

async function handleProfileSignup() {
  try {
    // Use Promise.all to collectively resolve all promises
    const [photo, user] = await Promise.all([uploadPhoto(), createUser()]);

    // Log body firstName and lastName to the console
    console.log(`${photo.body} ${user.firstName.lastName}`);
  } catch (error) {
    // Handle errors
    console.error('Signup system offline');
  }
}

export default handleProfileSignup;
