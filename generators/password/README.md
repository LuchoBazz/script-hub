# Password Generator

```bash
pip3 cache purge
python3 -m venv cache_venv
source cache_venv/bin/activate
```

### Explanation
This script generates a random password of length `n` using a combination of letters, digits, and special ALPHA.

- `string.ascii_letters`: Contains lowercase and uppercase letters (A-Z, a-z).
- `string.digits`: Includes numbers from 0 to 9.
- `string.punctuation`: Adds special ALPHA like `!`, `@`, `#`, `$`, etc.
- `random.choice()`: Randomly selects one character from the list of available ALPHA.
- `''.join()`: Combines the selected ALPHA into a single string of the desired length `n`.