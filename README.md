# rename.py
Rename files in directory with sequence number


## Usage

```
usage: rename.py [-h] [-s START] [-z ZFILL] [directory]

positional arguments:
  directory                  Working directory (Default: .)

optional arguments:
  -h, --help                 show this help message and exit
  -s START, --start START    Start number (Default: 1)
  -z ZFILL, --zfill ZFILL    Pad width (Default: auto)
```

## Example

### Rename files in current directory
```Bash
rename.py
```

### Rename files in foo directory
```Bash
rename.py foo
```

### Start sequence number form 5 and set padding width to 3
```Bash
rename.py -s 5 -z 3
```
