# War-Intensity-Index
 Script diário baseado em notícias sobre guerra

# War Intensity Analysis

This project collects headlines from Google News (RSS) about the Israel–Iran conflict and builds a simple **War Intensity Index** based on keyword mentions.

## What it does
- Fetches headlines automatically
- Counts keywords like `missile`, `drone`, `rocket`, `attack`
- Creates a `war_index`
- Saves the dataset to CSV (`data/war_news.csv`)

## How to run
```bash
pip install -r requirements.txt
python src/main.py
