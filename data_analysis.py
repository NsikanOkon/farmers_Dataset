#importing the packages
import pandas as pd
#import matplotlib.pyplot as plt

#reading of the excel file
df = pd.read_excel('jpil_farmers_dataset.xlsx', header=1)

#printing of the excel table
print(df)

#to see all columns
print('\n--- COLUMN NAMES ---')
print(df.columns.tolist())

#the data type of each column
print('\n--- DATA TYPE ---')
print(df.dtypes)

#check for missing values
print('\n--- missing values ---')
print(df.isnull().sum())

#working on the Yield Change Column
des_Yield_Change = df['Yield Change (%)'].describe()
print('\n--- des_Yield_Change ---')
print(des_Yield_Change)

#STATISTICS
#Working on the farm size
count = df['Farm Size (ha)'].count()
print('\n--- Farm Size(ha) count ---')
print(count)

#Average of farm size
avg_Farm_Size =df['Farm Size (ha)'].mean()
print('\n--- mean Farm Size (ha) ---')
print(avg_Farm_Size)

#Min of Farm Size
Min_Farm_Size =df['Farm Size (ha)'].min()
print('\n--- smallest Farm Size (ha) ---')
print(Min_Farm_Size)

#Max of Farm Size
Max_Farm_Size =df['Farm Size (ha)'].max()
print('\n--- largest Farm Size (ha) ---')
print(Max_Farm_Size)

#Median of Farm size
Median_Farm_Size =df['Farm Size (ha)'].median()
print('\n--- middle number of Farm Size (ha) ---')
print(Median_Farm_Size)

#Standard deviation of Farm Size
std_Farm_Size =df['Farm Size (ha)'].std().round(1)
print('\n--- std of Farm Size (ha) ---')
print(std_Farm_Size)

#Variance of Farm Size
variance_Farm_Size = df['Farm Size (ha)'].var()
print('\n--- variance of Farm Size (ha) ---')
print(variance_Farm_Size)

#total Farm Size
sum_Farm_Size = df['Farm Size (ha)'].sum()
print('\n--- sum of Farm Size (ha) ---')
print(sum_Farm_Size)