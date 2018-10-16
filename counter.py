""" A program that stores and updates a counter using a Python pickle file"""

import sys


def update_counter(file_name, reset=False):
    from os.path import exists
    from pickle import dump, load
    # fix global error
    """Update a counter stored in the file 'file_name'.

    A new counter will be created and initialized to 1 if none exists or if the
    reset True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    Parameters
    ----------
    file_name: str
        The file that stores the counter to be incremented.  If the file
        doesn't exist, a counter is created and initialized to 1.
    reset: bool
        True if the counter in the file should be reset.

    Returns
    -------
    int
        The new counter value

    Examples
    --------
    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """

    if reset is True or os.path.exists(file_name) :
        counter_file = open(file_name, 'wb') # opens the file in writing mode
        counter_file.counter = 1             # creates and initializes counter by 1
    else:
        counter_file = open(file_name, 'rb+') # opens the file in reading mode
        counter_file.counter = load(counter_file) # define what counter is
        counter_file.counter += 1             # increments counter by 1
        counter_file.seek(0, 0)               # move the file handle back to the beginning

    dump(counter_file.counter, counter_file)# store the resultant counter value to the disk

    return counter_file.counter


if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is {}".format(update_counter(sys.argv[1])))
