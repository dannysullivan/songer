from setuptools import setup

setup(name='songer',
      version='0.1',
      description='Song generator',
      url='https://github.com/dannysullivan/songer',
      author='Daniel Sullivan',
      author_email='danielalexandersullivan@gmail.com',
      license='MIT',
      packages=['songer'],
      install_requires=[
          'pymarkovchain',
          'pydub',
          'python-midi'
      ],
      zip_safe=False)
