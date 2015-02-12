class Action():
    """Represent a command line action"""

    callbacks = {}

    def __init__(self, name, args=None):
        self.name = name
        self.args = args

    def __call__(self, func):
        Action.callbacks[self.name] = (func, self.args)

        return func
