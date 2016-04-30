# rename.py
Rename files in directory with sequence number


## Usage

```
usage: rename.py [-h] [-c COUNT] [-p PREFIX] [-s SUFFIX] [-v] [-z ZFILL] [directory]

positional arguments:
  directory             Working directory (Default: .)

optional arguments:
  -h, --help                     show this help message and exit
  -c COUNT, --count COUNT        Initial count (Default: 1)
  -p PREFIX, --prefix PREFIX     Prefix
  -s SUFFIX, --suffix SUFFIX     Suffix
  -v, --verbose                  Verbose output
  -z ZFILL, --zfill ZFILL        Pad width (Default: auto)
```

## Example

### Rename files in current directory
```Bash
rename.py
```

### Rename files in current directory with verbose output
```Bash
rename.py -v
```

### Rename files in foo directory
```Bash
rename.py foo
```

### Start sequence number form 5 and set padding width to 3
```Bash
rename.py -c 5 -z 3
```
