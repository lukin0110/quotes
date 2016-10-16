Quotes
======

Small python package to read quote sets from csv files.

Installation
************

::

    pip install quotes
    
    
Usage
*****

Get a random quote:

.. code:: python

    from quotes import random

    if __name__ == '__main__':
        print(random())


List of available persons:

.. code:: python

    from quotes import persons

    if __name__ == '__main__':
        print(persons())