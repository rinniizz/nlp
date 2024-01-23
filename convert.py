import csv
import pandas as pd

file1_path = 'output.csv'
csv_file_path = 'convert2.csv'

df = pd.read_csv('output.csv', names=['text', 'sentiment'], header=None)

# Mapping function
def map_sentiment(value):
    sentiment_mapping = {
        1: 'pos',
        0: 'neu',
        -1: 'neg'
    }
    return sentiment_mapping.get(value, value)

# Apply the mapping function to the "sentiment" column
df['sentiment'] = df['sentiment'].apply(map_sentiment)

df = df[df['sentiment'] != 'q']
# Save the updated DataFrame to a new CSV file
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')
