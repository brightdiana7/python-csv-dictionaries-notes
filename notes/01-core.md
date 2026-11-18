# Read CSV into named fields: implementation

## What the example does

DictReader uses the header as keys. Validate duplicate headers before using this pattern for untrusted production files; this recipe uses unique headers.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"name,age\nAda,36\nLin,25\n"
```

Expected result:

```json
[
  {
    "name": "Ada",
    "age": "36"
  },
  {
    "name": "Lin",
    "age": "25"
  }
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
