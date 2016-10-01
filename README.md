# jsonlint

A JSON Linter in Python

# Installation

### Pre-Commit Hook

- `curl -so .git/hooks/pre-commit https://git.cssnr.com/shane/jsonlint/raw/master/jsonlint.py`
- `chmod +x .git/hooks/pre-commit`

### Windows

- http://cdn.cssnr.com/jsonlint/latest/dist/windows/jsonlint.exe

Download and move the executable to your %PATH% (example: `%SystemRoot%\system32`)

### Linux

- `curl -so /usr/local/bin/jsonlint http://cdn.cssnr.com/jsonlint/latest/dist/linux/jsonlint`
- `chmod +x /usr/local/bin/jsonlint`

### Mac

- `curl -so /usr/local/bin/jsonlint http://cdn.cssnr.com/jsonlint/latest/dist/mac/jsonlint`
- `chmod +x /usr/local/bin/jsonlint`

# Usage

Checks your current working directory recursively:

`jsonlint <file extension>`

Note the first argument is **optional** and defaults too: `.json`

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

# License

The MIT License (MIT)

Copyright (c) 2016 Shane

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
