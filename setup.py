from distutils.core import setup
import os
import vonny

setup(
    name='vonny',
    packages=['vonny'],
    python_requires='>=3',
    version=vonny.__version__,
    description='Text vonnytization',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Eugene Danini',
    author_email='e.danini@gmail.com',
    url="https://github.com/EugeneDanini/vonny",
    download_url='https://github.com/EugeneDanini/vonny/raw/master/dist/vonny-{}.tar.gz'.format(vonny.__version__),
    keywords=['humour', 'vonny', 'text'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
