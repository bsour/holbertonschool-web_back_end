export default function signUpUser(firstName, lastName) {
  const fName = firstName;
  const lName = lastName;
  return new Promise((resolve) => {
    resolve({
      firstName: fName,
      lastName: lName,
    });
  });
}
