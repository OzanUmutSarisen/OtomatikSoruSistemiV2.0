const fs = require('fs');

fs.readFile('Data.txt', 'utf-8', function (err, data) {

  if (err) throw err;

  console.log(data);

});