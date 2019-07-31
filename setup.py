#!/usr/bin/env python3

# Copyright (C) 2019 The Xaya developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from distutils.core import setup, Extension

neoscrypt_module = Extension('neoscrypt',
                               sources = ['neoscryptmodule.c',
                                          'neoscrypt.c'],
                               include_dirs=['.'])

setup (name = 'neoscrypt',
       version = '1.0',
       description = 'Bindings for the NeoScrypt proof-of-work algorithm',
       author = 'Autonomous Worlds Ltd',
       author_email = 'info@autonomousworlds.com',
       url = 'https://github.com/xaya/neoscrypt_python',
       ext_modules = [neoscrypt_module])
