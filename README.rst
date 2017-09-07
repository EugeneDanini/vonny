#####
vonny
#####
Text vonnytization
------------------
(supports cyrillic and latin)

Installation and usage
----------------------


.. code-block:: bash

    $ pip install vonny

or

.. code-block:: bash

    $ pip install dist/vonny-1.0.2.tar.gz


then

.. code-block:: python

    >>> from vonny.utils import vonnytize
    >>> print(vonnytize('Hello, World!'))
    Hllo, Wrld!