from functools import reduce


class BaseFit(object):
    """  This class avoid to write the fit method to every
    (BaseEstimator, TransformerMixin), child
    """
    def fit(self, x, y=None):
        """
        :param x: A set of values with text or tokens
        :param y: actual labels
        :return:
        """
        return self


class FunctionComposer(object):
    """ The idea of this class is compose 2 o more
    functions, in order to use it in a map pipeline
    :param functors:  a list of functions to compose
    """

    __slots__ = ('funcs',)

    def __init__(self, *functors):
        self.funcs = functors

    @staticmethod
    def dual_composition(f, g):
        """Compose two functions in one function
        :param f: takes the output of g(x)
        :param g: takes the value of x
        :return: compose functions
        """
        return lambda x: f(g(x))

    def __call__(self, text):
        """ Compose n functions and trigger the pipeline
        :param text: input of the composed function
        :return:
        """
        args = (self.dual_composition, self.funcs)
        return reduce(*args)(text)
