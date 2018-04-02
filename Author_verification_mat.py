# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:51:17 2018

@author: SAMEERGO
"""

#%%
import re
import sys
from collections import Counter
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
#%%

word_list = [ "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself", "me", "more", "most", "my", "myself", "of", "on", "once", "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "should", "so", "some", "such", "than", "that", "the", "their", "them", "themselves", "then", "there", "these", "they", "they'd", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "were", "what", "when", "which", "while", "who", "whom", "why", "with", "would", "you", "your", "yours", "yourself", "yourselves"]
#word_list = [ "about", "above" ]

word_matrix_train = []
vocab = []
common = []
#%%
  
def build_vocab_train (infile):
     input_text = open(infile, 'r')
     text_string = input_text.read().lower()
     match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
     #print(len(match_pattern),infile)
     cnt = Counter(match_pattern)
     #most_common = Counter(match_pattern).most_common(20)
     #most_common_words = [t[0] for t in most_common]
     word_freq = []
     global word_list
     global word_matrix_train      
     for word in word_list:
         word_freq.append(cnt[word]/len(match_pattern)*1000)
     word_matrix_train.append(word_freq)
     input_text.close()
       
#%%     
     
def build_vocab_question (infile):
     input_text = open(infile, 'r')
     text_string = input_text.read().lower()
     match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
     #print(len(match_pattern),infile)
     cnt = Counter(match_pattern)
     #most_common = Counter(match_pattern).most_common(20)
     #most_common_words = [t[0] for t in most_common]
     word_freq = []
     global word_list
     word_matrix_question = []
     for word in word_list:
         word_freq.append(cnt[word]/len(match_pattern)*1000)
     word_matrix_question.append(word_freq)
     input_text.close()
     return word_matrix_question
#%%       
#input in files - first argument - file having list of all input data-set files , second argument question data-set file
def author_verification():
    infile = sys.argv[1]
    qfile = sys.argv[2]
    actual = sys.argv[3]
    out = open('CV.txt',"a")
       
    with open(infile) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines] 
    for line in lines:
        build_vocab_train(line)
    global word_matrix_train
    
    distance = np.array(euclidean_distances(word_matrix_train,word_matrix_train))
    distance_len = len(distance[0] - 1)
    distance_train = np.sum(distance)/(distance_len*distance_len)
    check = build_vocab_question(qfile)
    #print(check)
    distance_question = np.array(euclidean_distances(word_matrix_train,check))
    distance_question = sum(distance_question.mean(axis=0))
    #print(distance_question)
    
    if  ((distance_question - distance_train) <= 3 and actual == '1'):
        #print(distance_question - distance_train)
        out.write("Correct\n")      
    elif ((distance_question - distance_train) > 3 and actual == '0'):
        #print(distance_question - distance_train)
        out.write("Correct\n")
    else:
        #print(distance_question - distance_train)
        out.write("Incorrect\n")
        


    #print(len(vocab))
    f.close()
    out.close()
      
#%%
    
author_verification()