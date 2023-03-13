#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if num % 2 == 0]
    print(evens)
    return evens


def make_exclamation(sentence_list):
    sentence_with_exclamation = [(sentence + "!") for sentence in sentence_list]
    print(sentence_with_exclamation)
    return sentence_with_exclamation