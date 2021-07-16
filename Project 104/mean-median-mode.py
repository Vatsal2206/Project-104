import statistics as stc
import csv
with open('SOCR-HeightWeight.csv', newline='') as f:
     reader = csv.reader(f)
     file_data = list(reader)

file_data.pop(0)

sort_data = []

for index in range(len(file_data)):
     num = file_data[index][1]
     sort_data.append(float(num))

# Calculate Mean

mean = sum(sort_data)/len(sort_data)
print("Mean is : ", mean)

# Calculate Median

median = stc.median(sort_data)
print("Median is : ", median)

# Calculate Mode

mode = stc.mode(sort_data)
print("Mode is : ", mode)