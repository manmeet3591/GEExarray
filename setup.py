from setuptools import setup

setup(name='geexarray',
      version='0.1',
      description='Convert earth engine collection objects to xarrays',
      url='https://github.com/tam-borine/GEExarray',
      author='Tam Borine and Tommy Lees',
      author_email='',
      license='MIT',
      packages=['geexarray'],
      install_requires=[
          'earthengine-api',
          'xarray'
        ],
      zip_safe=False)