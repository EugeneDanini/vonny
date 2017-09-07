from distutils.core import setup
import vonny

setup(
    name='vonny',
    packages=['vonny'],
    python_requires='>=3',
    version=vonny.__version__,
    description='Text vonnytization',
    author='Eugene Danini',
    author_email='e.danini@gmail.com',
    url='https://github.com/EugeneDanini/vonny',
    download_url='https://github.com/EugeneDanini/vonny/dist/%s.tar.gz'.format(vonny.__version__),
    keywords=['humour', 'vonny', 'text'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
