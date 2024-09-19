process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (input) => {
  const name = input.toString().trim();

  // Output the name without automatically adding a new line
  process.stdout.write(`Your name is: ${name}\r\n`);

  // Check if input is coming from a non-TTY (piped input)
  if (!process.stdin.isTTY) {
    process.stdout.write('This important software is now closing\r\n');
  }

  process.exit();
});
