// THE CALLBACK VERSION
const fakeRequestCallback = (url, success, failure) => {
  const delay = Math.floor(Math.random() * 4500) + 500;
  setTimeout(() => {
    if (delay > 4000) {
      failure('Connection Timeout :(');
    } else {
      success(`Here is your fake data from ${url}`);
    }
  }, delay);
};
// THE PROMISE VERSION
const fakeRequestPromise = url => {
  return new Promise((resolve, reject) => {
    const delay = Math.floor(Math.random() * 4500) + 500;
    setTimeout(() => {
      if (delay > 4000) {
        reject('Connection Timeout :(');
      } else {
        resolve(`Here is your fake data from ${url}`);
      }
    }, delay);
  });
};
// Using callbacks
fakeRequestCallback(
  'books.com/page1',
  success => {
    console.log('First success');
    console.log(success);
    fakeRequestCallback(
      'books.com/page2',
      success => {
        console.log('Second success');
        console.log(success);
        fakeRequestCallback(
          'books.com/page3',
          success => {
            console.log('Third success');
            console.log(success);
          },
          failure => {
            console.log('Third failure');
            console.log(failure);
          }
        );
      },
      failure => {
        console.log('Second failure');
        console.log(failure);
      }
    );
  },
  failure => {
    console.log('First failure');
    console.log(failure);
  }
);

// THE CLEANEST OPTION WITH THEN/CATCH
// RETURN A PROMISE FROM .THEN() CALLBACK SO WE CAN CHAIN!

fakeRequestPromise('tibia.com/page1')
  .then(data => {
    console.log(data);
    return fakeRequestPromise('tibia.com/page2');
  })
  .then(data => {
    console.log(data);
    return fakeRequestPromise('tibia.com/page3');
  })
  .then(data => {
    console.log(data);
  })
  .catch(err => {
    console.log(err);
  });
