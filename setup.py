from distutils.core import setup

setup(
    name='bitio',
    version='0.1',
    packages=['src.microbit', 'src.microbit.repl', 'src.microbit.serial', 'src.microbit.serial.tools',
              'src.microbit.serial.threaded', 'src.microbit.serial.urlhandler', 'src.microbit.portscan'],
    url='https://github.com/whaleygeek/bitio',
    license='',
    author='David Whale',
    author_email='',
    description=''
)
