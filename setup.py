from setuptools import setup

setup(name='autism',
      version='0.1',
      description='autism module',
      url='vk.com/alexkryu4kov',
      author='Alexey Kryuchkov',
      author_email='alexkryu4kov@gmail.com',
      license='MIT',
      packages=['database', 'mail', 'algo'],
      install_requires=['flask>=1.0.2', 'sqlalchemy', 'flask_sqlalchemy', 'psycopg2'],
      zip_safe=False)
