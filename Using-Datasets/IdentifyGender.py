# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 01:37:50 2016

@author: varshith
"""

country_code = input('Enter country code :')
name = input('Enter name :')

from gender_detector import GenderDetector
detector = GenderDetector(country_code) # It can also be ar, uk, uy.
detector.guess(name) # => 'male'