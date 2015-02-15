Helpgen
=======

**helpgen** helps you to make easily help/usage message of command line tools.

Example
-------

Next is a short example of how to use the library :
::

    #!/usr/bin/env python

    import sys

    from helpgen.decorators import Action
    from helpgen.parser import ActionParser


    @Action('test')
    def action_test():
        """run a test"""

        print("I AM A TEST \o/")


    @Action('hello', args=['word'])
    def action_hello(word):
        """display a word"""

        print("The word is : %s" % (word,))


    def main():
        parser = ActionParser(description="helpgen test script")
        parser.compile()

        try:
            parser.process()
        except:
            return 1
        else:
            return 0

    if __name__ == "__main__":
        sys.exit(main())

This peace of code will produce these help messages :

- generic help message:

::

    $ ./test.py -h
    usage: test.py [-h] {test,hello} ...

    helpgen test script

    positional arguments:
      {test,hello}
        test        run a test
        hello       display a word

    optional arguments:
      -h, --help    show this help message and exit

- help message for test sub command:

::

    $ ./test.py test -h
    usage: test.py test [-h]

    optional arguments:
      -h, --help  show this help message and exit

- help message for hello sub command:

::

    $ ./test.py hello -h
    usage: test.py hello [-h] word

    positional arguments:
      word

    optional arguments:
      -h, --help  show this help message and exit

- and, it works fine :

::

    $ ./test.py test
    I AM A TEST \o/
    $ ./test.py hello "\_o<~ KOIN"
    The word is : \_o<~ KOIN

