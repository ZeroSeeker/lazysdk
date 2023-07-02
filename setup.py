#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="lazysdk",
    version="0.1.18",
    description="基于Python的懒人包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ZeroSeeker",
    author_email="zeroseeker@foxmail.com",
    url="https://gitee.com/ZeroSeeker/lazysdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'showlog>=0.0.6',
        'requests==2.27.1',
        'envx>=1.0.1',
        'pytz==2022.1',
        'redis==4.1.0',
        'ua_parser==0.10.0',
        'openpyxl==3.0.9',
        'xlrd==2.0.1',
        'numpy==1.22.0',
        'm3u8==3.5.0',
        'pycryptodome==3.10.1'
    ]
)
