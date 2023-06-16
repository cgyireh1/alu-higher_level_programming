#!/usr/bin/node

const num = parseInt(process.argv[2], 10);
if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = num; i > 0; i -= 1) {
    console.log('C is fun');
  }
<<<<<<< HEAD
} 
=======
}
>>>>>>> 8ad2233955416c537847a7a51510637a9a183ea5
