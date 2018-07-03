#!/usr/bin/env python

try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

setup(name="pywandevent",
	version="1.0",
	description = "Python implementation of libwandevent",
	author = "Shane Alcock",
	author_email = "contact@wand.net.nz",
	url="http://www.wand.net.nz",
	packages = ['pywandevent'],
	package_dir = {
		'pywandevent':'pywandevent'
	}
)


