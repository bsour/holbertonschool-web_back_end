function getResponseFromAPI() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('true');
    }, 300);
  });
}

const responsePromise = getResponseFromAPI(); // Call the function

responsePromise
  .then((response) => {
    console.log(response);
  })
  .catch((error) => {
    console.error(error);
  });
