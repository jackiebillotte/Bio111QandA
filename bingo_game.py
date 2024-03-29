#!/usr/bin/python3

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import random
import csv
import os

st.markdown(""" <style> .font {
font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} 
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font">BIO 111 Review</p>', unsafe_allow_html=True)

filename = st.sidebar.text_input('Custom Question Set')
try:
	with open(filename) as input:
		dict = pd.read_csv(csvfile, header=None, index_col=0, squeeze=True).to_dict()
except FileNotFoundError:
	with open('bingo_key.csv', newline='') as csvfile:
		dict = pd.read_csv(csvfile, header=None, index_col=0, squeeze=True).to_dict()
length= len(dict)
numbers = list(range(1, length))

def fun():
	i= np.random.randint(1,length)
	if i in numbers:
		st.header("*%s*" %  dict.get(i))
		numbers.remove(i)
		return numbers
	else:
		st.write("Spin again")


	
if st.sidebar.button("Select Question"):
	fun()
