function getResponseFromAPI() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('true');
    }, 300);
  });
}
