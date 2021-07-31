import math
import csv
with open('projectData.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    #sorting the data to get the list

data = file_data[0]
#getting the mean
def mean(data):
    n = len(data)
    total = 0 
    for x in data:
        total+= int(x)
        mean = total/n
        return mean

        # squaring the getting the value
squared_list =[]
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squared_list.append(a)
    # getting the sum
    sum = 0
    for i in squared_list:
        sum = sum + i
        #diving the sum by the number of terms
        result = sum/(len(data)-1) 
        # getting the edeviation by taking the square root of result
std_deviation = math.sqrt(result)
print(std_deviation)