Vonny package
Text vonnytization (supports cyrillic and latin)

Installation:
$ pip install vonny
or (replace * with proper version)
$ pip install dist/vonny-*.tar.gz

Usage:
>>> from vonny import vonnytize
>>> print(vonnytize('Hello, World!'))
Hllo, Wrld!
>>> print(vonnytize('Привет, Пятачок'))
Првт, Птчк
or
$ python vonny "Hello, world!"
Hllo, wrld!
$ python vonny "Привет, Пятачок"
Првт, Птчк
