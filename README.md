Helpgen
=======

Example
-------

This is a short example of how to use the library :

```python
#!/usr/bin/env python

import sys

from helpgen.decorators import Action
from helpgen.parser import ActionParser


@Action('test')
def action_test():
    """run a test"""

    print("I AM A TEST \o/")

def main():
    parser = ActionParser(description="helpgen test script")

    parser.process()

    return 0

if __name__ == "__main__":
    sys.exit(main())
```


This peace of code will produce :

```
$ ./test.py -h
usage: test.py [-h] {test} ...

helpgen test script

positional arguments:
  {test}
      test      run a test

	  optional arguments:
	    -h, --help  show this help message and exit
```

```
$ ./test.py test
I AM A TEST \o/
```
