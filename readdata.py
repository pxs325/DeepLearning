# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:15:41 2016

@author: GPU project
"""

import numpy as np

arr = np.loadtxt('airflow.csv',delimiter=',')

arr1 = np.array([[1.,2.,3],[4.,5.,6.],[7.,8.,9.]])

arr_slice = arr1[1:2,:2].copy()

print(arr_slice)