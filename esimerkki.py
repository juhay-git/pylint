"""_summary_

Returns:
    _type_: _description_
"""

# esimerkki.py

def add(a, b):
    """_summary_
        adds a and b together
    """
    return a+b

def subtract(a, b): # Subtracts b from a
    """_summary_
        adds a and b together
    """
    return a-b

def multiply(a, b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    return a * b

class OmaLuokka:
    """_summary_
    """
    def __init__(self, x):
        """_summary_

        Args:
            x (_type_): _description_
        """
        self.x = x

    def double_value(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.x * 2

    def print_x(self):
        """_summary_

        Args:
            x (_type_): _description_
        """
        print(self.x)

def main():
    """_summary_
    """
    x = 5
    olio = OmaLuokka(x)
    print(olio)

if __name__ == '__main__':
    main()
