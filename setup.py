from distutils.core import setup

setup(
    name='kamebot',
    version='1.1',
    description='make file with stdio and send it to slack',
    author='masaponto',
    author_email='masaponto@gmail.com',
    url='masaponto.github.io',
    install_requires=['slacker'],
    py_modules = ["kamebot"],
    package_dir = {'': 'src'}
)
