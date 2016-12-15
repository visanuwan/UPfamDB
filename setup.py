from setuptools import setup, find_packages

setup(
    name='UP',
    version='0.1',
    description='It is a database',
    # Project's main homepage.
    url='',
    packages=find_packages(exclude=["bin", "build", "data", "dist", "kali.egg-info",
                                    "logs", "results", "scripts", "tests"]),
    license='Apache License 2.0',
    scripts=["bin/upapp"],
    install_requires=['h5py==2.6.0',
                      'tables==3.3.0',
                      'pandas==0.19.1',
                      'flask=0.11.1',
                      'Flask==0.11.1',
                      'Flask-RESTful==0.3.5'
                     ])
