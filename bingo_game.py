#!/usr/bin/python3

import streamlit as st
import numpy as np
import pandas as pd
import random
import csv

st.markdown(""" <style> .font {
font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} 
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font">BIO 111 Bingo Review</p>', unsafe_allow_html=True)


#st.title("BIO 111 Final Review Bingo")



#Read in data
#import csv
with open('bingo_key.csv', newline='') as csvfile:
		dict = pd.read_csv(csvfile, header=None, index_col=0, squeeze=True).to_dict()
	
numbers = list(range(1, 40))
def fun():
	i= np.random.randint(1,40)
	if i in numbers:
		st.header("*%s*" %  dict.get(i))
		numbers.remove(i)
		return numbers
	else:
		st.write("Spin again")


	
if st.sidebar.button("Select Question"):
	fun()
