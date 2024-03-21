class MyClass:
    """
    This is a sample class demonstrating the usage of numpy docstring format.

    Parameters
    ----------
    param1 : int
        Description of param1.
    param2 : str
        Description of param2.

    Attributes
    ----------
    attribute1 : float
        Description of attribute1.
    attribute2 : list of int
        Description of attribute2.

    Methods
    -------
    method1(arg1, arg2)
        Description of method1.
    method2(arg)
        Description of method2.

    Examples
    --------
    >>> obj = MyClass(5, 'example')
    >>> obj.method1(2, 3)
    6
    """
    
    def __init__(self, param1, param2):
        """
        Initialize MyClass with param1 and param2.

        Parameters
        ----------
        param1 : int
            Description of param1.
        param2 : str
            Description of param2.
        """
        self.attribute1 = 0.0
        self.attribute2 = [1, 2, 3]

    def method1(self, arg1, arg2):
        """
        Perform some operation using arg1 and arg2.

        Parameters
        ----------
        arg1 : int
            Description of arg1.
        arg2 : int
            Description of arg2.

        Returns
        -------
        int
            Result of the operation.
        """
        return arg1 + arg2

    def method2(self, arg):
        """
        Perform another operation using arg.

        Parameters
        ----------
        arg : str
            Description of arg.

        Returns
        -------
        str
            Result of the operation.
        """
        return "Result: " + arg
