from setuptools import setup


setup(
    name='gitsnapshot',
    version='0.1.1',
    description='Python module to simplify loading of snapshot of git repository',
    author='Kirill Sulim',
    author_email='kirillsulim@gmail.com',
    license='MIT',
    url='https://github.com/kirillsulim/gitsnapshot',
    py_modules=['gitsnapshot'],
    test_suite='tests',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Version Control :: Git',
    ],
    keywords='git snapshot load download delivery config',
)
