from distutils.core import setup

setup(
    name='kamebot',
    version='1.0',
    description='make file with stdio and send it to slack',
    author='masaponto',
    author_email='masaponto@gmail.com',
    url='masaponto.github.io',
    install_requires=['slacker'],
    py_modules = ["kame_bot"],
    package_dir = {'': 'src'}
)
