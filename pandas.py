# What is Pandas? 

# * Pandas is a Python library.
# * Pandas is used to analyze data.
# * The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

#************************************************
#  importing pandas library

import pandas as pd

# Creating a DataFrame
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)


#  Creating a Series
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)


# Checking pandas version
print(pd.__version__)


# BASIC COMMANDS IN PANDAS


# 1.To read a csv(Comma Seperted Value) files 
df = pd.read_csv('path of the csv file') #it just reads the files does nothing in the output.
print(df.to_string()) # to_string() method prints all the contents in the file.


# 2. To change the labels of the columns or rows 
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])


# 3. Pandas use the loc attribute to return one or more specified row(s)
print(df.loc[0])
print(df.loc[[0, 1]]) # it returns both first and second row


# 4. With the index argument, you can name your own indexes.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 


# 5. To know how many no of rows your system display at a time
print(pd.options.display.max_rows) 


# 6. To read JSON files 
df = pd.read_json('data.json')
print(df.to_string()) 


# 7. The head() method returns the headers and a specified number of rows, starting from the top.
df = pd.read_csv('data.csv')
print(df.head(10)) # It returns first ten lines in the file from the top
# by default the ".head()" function returns only topmost 5 lines if no number is specified in the ().
# ** Similarly "".tail()" reverse of head function. **


#  8. A method called info(), that gives you more information about the data set.
print(df.info()) 


# 9. The dropna() method returns a new DataFrame, and will not change the original.
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string()) #If you want to change the original DataFrame, use the inplace = True argument:

df = pd.read_csv('data.csv')
df.dropna(inplace = True)
print(df.to_string()) #Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.
df.dropna(subset=['Date'], inplace = True) # It Remove rows with a NULL value in the "Date" column.


# 10. The fillna() method allows us to replace empty cells with a value inside ().
df.fillna(0, inplace = True)

#To only replace empty values for one column, specify the column name for the DataFrame:
df = pd.read_csv('data.csv')
df["Column Name"].fillna(0, inplace = True)


# 11. The mean() median() and mode() methods to calculate the respective values for a specified column.
x = df["Column Name"].mean() # Similarly ".mode()" ; ".median()" .











