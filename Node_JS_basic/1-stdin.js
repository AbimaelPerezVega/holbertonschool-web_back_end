const readline = require('readline');

// Set up the input/output interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Welcome to Holberton School, what is your name?\n', (name) => {
  console.log(`Your name is: ${name}`);
  rl.close();
});

// Detect when the interface is closed and print the closing message
rl.on('close', () => {
  console.log('This important software is now closing');
  process.exit(0);
});
