from setuptools import setup


setup(name='staellning',
      version='0.1',
      description='Scaffolding in real-time',
      url='http://github.com/emilhaegglund/staellning',
      author='Emil Haegglund',
      license='',
      install_requires=[
        'bokeh',
        'watchdog'],
      scripts=['bin/staellning']
      )