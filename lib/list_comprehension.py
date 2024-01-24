#!/usr/bin/env python3

def return_evens(num_list):
    return [i for i in range(0,num_list,2)]

def make_exclamation(sentence_list):
    return [i +"!" for i in sentence_list]


print(return_evens(10))

print(make_exclamation(["bird", "i am cat"]))