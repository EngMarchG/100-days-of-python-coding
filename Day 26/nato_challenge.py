from matplotlib.font_manager import list_fonts
import pandas as pd


data = pd.read_csv("100 days of python\\Day 26\\nato_list.csv")

phonetic = {row.letter:row.code for (index,row) in data.iterrows()}

name = input("What is your name? ").upper()
listo=[]
for letter in name:
    print(f"{letter} for {phonetic[letter]}")
    listo.append(phonetic[letter])
print(listo)
