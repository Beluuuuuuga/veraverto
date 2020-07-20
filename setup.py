import setuptools
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(  
    name="veraverto",  
    version="0.0.1",  
    author="beluga",  
    author_email="inoue.koki15@gmail.com",  
    description="BOT and CLI framework for handling multiple services in python",  
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    url="https://github.com/Beluuuuuuga/veraverto",  
    packages=setuptools.find_packages(),  
    classifiers=[  
        "Programming Language :: Python :: 3.7",  
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",  
    ],  
)  
