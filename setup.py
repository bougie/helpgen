from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='helpgen',
      version='0.1',
      description="""Argparse frontend library to help making software
usage message""",
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
      ],
      keyworkds='argparse help usage',
      url='https://github.com/bougie/helpgen',
      author='David Hymonnet',
      author_email='bougie@appartland.eu',
      license='BSD',
      packages=['helpgen'],
      include_package_data=True,
      zip_safe=False)
