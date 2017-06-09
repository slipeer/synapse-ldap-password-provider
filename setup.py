#!/usr/bin/env python

# Copyright 2017 Slipeer <slipeer@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
from codecs import open
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="synapse_ldap_password_provider",
    version="1",
    py_modules=["synapse_ldap_password_provider"],
    description="LDAP3 password provider for Synapse",
    install_requires=[
        "Twisted>=15.1.0",
        "ldap3>=2",
        "service_identity",
    ],
    long_description=read("README.rst"),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Topic :: Communications :: Chat'
    ],
)
