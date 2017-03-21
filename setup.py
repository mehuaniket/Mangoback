#!/usr/bin/env python

from setuptools import setup

setup(
    name="mangoback",
    version="0.1.0",
    description="Purpose of this mongoback library is to make it easy for user to take backup from one instace and restore it on another instance by just configuring one config file.",
    author="Aniket patel",
    author_email="patelaniket165@gmail.com",
    url="",
    packages=["mangoback"],
    download_url="https://github.com/kodani/mangoback",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: IOT developers and automation",
        "Programming Language :: Python",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: mongodb :: local to remote backup ::backup on instance",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries"
    ],
    install_requires=["colorama"]
)
