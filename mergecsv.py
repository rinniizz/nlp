import csv
import pandas as pd

# กำหนดชื่อไฟล์ text ทั้งสอง
file1_path = './train.txt'
file2_path = './train_label.txt'
dat = {'text': [], 'sentiment': []}

# อ่านข้อมูลจากไฟล์1
with open(file1_path, 'r', encoding='utf-8') as file1:
    data1 = file1.readlines()
    dat['text'] = data1

# อ่านข้อมูลจากไฟล์2
with open(file2_path, 'r', encoding='utf-8') as file2:
    data2 = file2.readlines()
    dat['sentiment'] = data2

csv_file_path = 'output.csv'

# เขียนข้อมูลลงในไฟล์ CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
    csv_writer = csv.writer(csv_file)

    # เขียนหัวข้อคอลัมน์

    # เขียนข้อมูลลงในไฟล์ CSV
    for i in range(len(dat['text'])):
        csv_writer.writerow([dat['text'][i].strip(), dat['sentiment'][i].strip()])

print(f'ไฟล์ CSV ถูกสร้างที่: {csv_file_path}')

