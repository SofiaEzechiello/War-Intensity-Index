import feedparser
import pandas as pd

# busca notícias sobre guerra
rss_url = "https://news.google.com/rss/search?q=Israel+Iran+war&hl=en-US&gl=US&ceid=US:en"

feed = feedparser.parse(rss_url)

data = []

for entry in feed.entries:
    data.append({
        "title": entry.title,
        "date": entry.published
    })

df = pd.DataFrame(data)

# palavras relacionadas a guerra
keywords = ["missile", "rocket", "drone", "airstrike", "attack"]

for k in keywords:
    df[k] = df["title"].str.lower().str.count(k)

# índice simples de guerra
df["war_index"] = df[keywords].sum(axis=1)

print(df)

df.to_csv("war_news.csv", index=False)

print("Arquivo salvo: war_news.csv")