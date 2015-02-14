import argparse
import helpgen.decorators


class ActionParser(argparse.ArgumentParser):
    """Extend `argparse.ArgumentParser`"""

    def __init__(self, *args, **kwargs):
        super(ActionParser, self).__init__(*args, **kwargs)

    def compile(self):
        """Generate arguments list from `Action` list"""

        subparsers = self.add_subparsers(dest='sub_commands')
        for name, (f, fargs) in helpgen.decorators.Action.callbacks.items():
            _parser = subparsers.add_parser(name, help=f.__doc__)
            if fargs is not None:
                for argname in fargs:
                    _parser.add_argument(argname, default=None)

    def process(self, *args, **kwargs):
        """Call the function associated to the sub_command passed in sys.argv
        and return the function response"""

        response = None
        pargs = self.parse_args(*args, **kwargs)

        if pargs.sub_commands in helpgen.decorators.Action.callbacks.keys():
            (f, fargs) = helpgen.decorators.Action.callbacks[pargs.sub_commands]
            if fargs is not None:
                response = f(**{_: getattr(pargs, _, None) for _ in fargs})
            else:
                response = f()

        return response
