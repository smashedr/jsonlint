# jsonlint

A JSON Linter in Python

# Installation

### Windows

Download and move the executable to your %PATH% (example: `%SystemRoot%\system32`)
- http://cdn.cssnr.com/jsonlint.exe

### Linux/Mac

Add to git hooks with:

- `curl -so .git/hooks/pre-commit https://git.cssnr.com/shane/jsonlint/raw/master/jsonlint.py`
- `chmod +x .git/hooks/pre-commit`

Add to system with:

- `curl -so /usr/local/bin/jsonlint https://git.cssnr.com/shane/jsonlint/raw/master/jsonlint.py`
- `chmod +x /usr/local/bin/jsonlint`

# Usage

Checks your current working directory recursively:

`jsonlint <file extension>`

Note the first argument is optional and defaults too: `.json`

### Examples

```
C:\Users\Shane\tmp\test> jsonlint
Checking C:\Users\Shane\tmp\test\good.json
No JSON errors detected.
```

```
C:\Users\Shane\tmp\test> jsonlint .conf
Checking C:\Users\Shane\tmp\test\conf\good-json-1.conf
Checking C:\Users\Shane\tmp\test\conf\good-json-2.conf
No JSON errors detected.
```

```
C:\Users\Shane\tmp\test> jsonlint .txt
Checking C:\Users\Shane\tmp\test\not-json.txt

-- JSON parse error
-- File: C:\Users\Shane\tmp\test\not-json.txt
-- Info: Expecting value: line 1 column 1 (char 0)

Commit aborted by: C:\bin\jsonlint.exe
```
