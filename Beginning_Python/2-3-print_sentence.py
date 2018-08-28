#!/usr/bin/env python3
sentence = input("Sentence: ")
screen_with = 80
len_sentence = len(sentence)
box_with = len_sentence + 6
left_margin = (screen_with - box_with) // 2
print()
print(' ' * left_margin + "+" + "-" * (box_with -2) + "+")
print(' ' * left_margin + "|" + " " * 2 + " " * len_sentence + " " * 2 + "|")
print(' ' * left_margin + "|" + " " * 2 + sentence + " " * 2 + "|")
print(' ' * left_margin + "|" + " " * 2 + " " * len_sentence + " " * 2 + "|")
print(' ' * left_margin + "+" + "-" * (box_with -2) + "+")