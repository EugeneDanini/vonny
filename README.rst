#####
vonny
#####
Text vonnytization
------------------
(supports cyrillic and latin)

.. image:: https://github.com/EugeneDanini/vonny/raw/master/vonny.jpg
    :alt: Vonny

Installation and usage
----------------------


.. code-block:: bash

    $ pip install vonny

or (replace * with proper version)

.. code-block:: bash

    $ pip install dist/vonny-*.tar.gz


then

.. code-block:: python

    >>> from vonny.utils import vonnytize
    >>> print(vonnytize('Hello, World!'))
    Hllo, Wrld!