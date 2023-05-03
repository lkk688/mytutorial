"""
Python sample.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def testpy_function(kind=None):
    """
    Return a list of random strings.

    :param kind: Optional.
    :type kind: list[str] or None
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "test"]
