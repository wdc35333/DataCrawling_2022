#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
import csv

def openfile(fname):
    f = open(fname, "r")
    data = list(csv.reader(f))
    f.close()

    return data
if __name__ == "__main_":
    rdf = openfile(fname)
    cnt = 0
    for line in rdf:
        cnt += 1
        print(line)
        if cnt == 10:
            break


# In[ ]:




