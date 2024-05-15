from setuptools import setup, find_packages

setup(name='ms_identity_web',
      version='0.16.6',
      description='MSAL Identity Utilities',
      author='Tobias',
      url='https://github.com/TobiasInvictus/ms-identity-python-common',
      packages=find_packages(),
      install_requires=['msal>=1.6.0,<2'],
     )


