# xrange for python 3

class xrange(object):
    def __init__(self, *args):
        self.args = args
        self.start = 0
        self.stop = 0
        self.step = 1
        if len(args) == 1:
            self.stop = args[0]
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise TypeError("xrange expected at most 3 arguments, got {}".format(len(args)))
        self.i = self.start
        self.n = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.stop:
            raise StopIteration
        self.n = self.i
        self.i += self.step
        return self.n


if __name__ == "__main__":
    for i in xrange(10):
        print(i)
