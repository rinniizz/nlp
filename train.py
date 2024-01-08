import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# อ่านข้อมูลจากไฟล์ CSV
df = pd.read_csv('output.csv', names=['text', 'sentiment'], header=None)

# ตรวจสอบข้อมูลที่ถูกอ่าน
print(df)

# ตรวจสอบค่าที่มีในคอลัมน์ 'sentiment'
print(df['sentiment'].unique())

df['sentiment'].value_counts().plot.bar()