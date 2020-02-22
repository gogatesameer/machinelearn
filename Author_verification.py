# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 13:24:53 2018

@author: SAMEERGO
"""

#%%
import re
import sys
from collections import Counter
#%%

vocab = []
min_wordcnt = 1000
max_wordcnt = 0
min_length = 100
max_length = 0
prev_len = 0
rate = 0
rate_prev = 0
        
#%%
      
def build_vocab (infile):
     input_text = open(infile, 'r')
     text_string = input_text.read().lower()
     match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
     #print(len(match_pattern),infile)
     cnt = list (Counter(match_pattern))
     global vocab
     global prev_len
     global rate
     global rate_prev
     rate_prev = rate
     prev_len_tmp = prev_len
     prev_len = len(vocab)
     
     for word in cnt:
         if word not in vocab:
             vocab.append(word)
     
     #print (len(vocab))
     #print(prev_len - prev_len_tmp)
     rate = ((len(vocab) - prev_len) /len(match_pattern))
     print (rate,rate_prev)
     if (((len(vocab)) - prev_len) < (prev_len - prev_len_tmp +50 ) and rate < rate_prev):
         return 1
     return 0
#%%
#input in files - first argument - file having list of all input data-set files , second argument question data-set file
def author_verification():
    infile = sys.argv[1]
    qfile = sys.argv[2]
    with open(infile) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines] 
    for line in lines:
        build_vocab(line)
    
    check = build_vocab(qfile)
    
    if check == 1:
        print("Author of dataset & question paragraph looks to be same")
    else:
        print("Authors of dataset & question paragraph look to be different")
              
#%%
    
author_verification()