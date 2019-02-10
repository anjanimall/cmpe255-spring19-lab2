
# coding: utf-8

# In[127]:


matplotlib inline


# In[7]:


import statistics

def mean_num_friends(x):
    return (sum(x) / float(len(x)))

def median_num_friends(x):
    return statistics.median(x)

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]

# sorted list: [4, 5, 7, 10, 20, 25, 40, 41, 49, 60, 100]
# ANS mean: 32.8
# ANS median: 25

print("mean={}".format(mean_num_friends(num_friends)))
print("median={}".format(median_num_friends(num_friends)))

