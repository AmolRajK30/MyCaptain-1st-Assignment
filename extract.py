# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 23:33:12 2023

@author: roney
"""

import os
path = 'C:/Amol Raj/Study/My Captain/Python Programming/extract.py'
result = os.path.splitext(path)
print('Path: ',result[0])
print('Extension: ', result[1])
