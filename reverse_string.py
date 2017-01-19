"""Reversing a string.

This is a variety of different functions to reverse a string. Some will print
the reversed string, others will return the value.  

"""

def rev_print(string):
    """Prints a string in reverse (with spaces between characters), using a for loop.
    
        >>> rev_print('hello')
        o l l e h

    """

    for i in range(-1, -(len(string) + 1), -1):
        print string[i],


def rev_print_splice(string):
    """Prints a string in reverse (without spaces), using a string splice.
        
        >>> rev_print_splice('hello')
        olleh

    """

    print string[::-1]



def rev_loop(string):
    """Returns the string, reversed, but completed not in place.

        >>> rev_loop('hello')
        'olleh'

    """

    new_str = ''

    str_len = len(string)

    for i in range(-1, -(str_len + 1), -1):
        new_str += string[i]

    return new_str


def rev_return_splice(string):
    """Returns a reversed string using string splicing.

        >>> rev_return_splice('foobar')
        'raboof'

    """

    return string[::-1]


def rev_recur(string):
    """Returns the string reversed, using recursion.
        
        >>> rev_recur('yes')
        'sey'

    """

    if not string:
        return string

    return rev_recur(string[1:]) + string[0]


def rev_recur2(string):
    """Returns the string reversed, using recursion.

        >>> rev_recur2('tuba')
        'abut'

    """

    if len(string) < 2:
        return string

    return string[-1] + rev_recur2(string[1:len(string) - 1]) + string[0]


def reverse1(string):
    """Returns the string reversed.

        >>> reverse1('foobar baz')
        'zab raboof'

    """

    str_len = len(string)
    halfway = int(str_len/2)
    
    char = [item for item in string]
    
    for i in range(halfway):
        char[i], char[str_len - 1 - i] = char[str_len - 1 - i], char[i]

    string = ''.join(char)
    
    return string


def reverse2(string):
    """Returns the string reversed, without recursion, using string splicing.

    >>> reverse2('TACocat')
    'tacoCAT'

    """
    
    s_len = int(len(string)/2)
    
    for i in range(1, s_len + 1):        

        string = (string[:i-1] + 
                 string[len(string) - i] + 
                 string[i: len(string) - i] +          
                 string[i-1] +
                 string[len(string) - i + 1:])

    return string


#####################################################################
# Docstring tests 

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

