import numpy as np
import pandas as pd

df = pd.read_csv('anime.csv')
df.head()

print(np.__version__)
print(pd.__version__)

#Hard way
def extract_eps(text):
    check = False
    episode = ''
    for i in text:
        if i == ')':
            break
        if i == '(':
            check = True
        if check:
            episode += i
    return episode

df['Episode'] = df['Title'].apply(extract_eps)

#Syntax frendly way
df['Episode'] = df['Title'].str.extract(r'\((\d+) eps\)')
df["Episode"] = df["Episode"].astype(int)

date_pattern = r'([A-Z][a-z]{2}\s\d{4})'

df["TimeStamp"] = df['Title'].str.extract(r'([A-Z][a-z]{2}\s\d{4}\s-\s[A-Z][a-z]{2}\s\d{4})')
Highest_Score = df[df["Score"] == df["Score"].max()]
Highest_Episode = df[df["Episode"] == df["Episode"].max()]

top_5_episodes = df.nlargest(5, 'Episode')[['Title', 'Episode']]

print("--- Top 5 Anime by Episode Count ---")
print(top_5_episodes)

print(Highest_Score)
print(Highest_Episode)

print(df["Title"].head())
