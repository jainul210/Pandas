import pandas as pd
import numpy as np
# arr = np.array([[1, 2], [3, 4]])
# df = pd.DataFrame(arr, columns=["A", "B"])
# # print(df)
# a = df["A"]
# print(a)

# data = {
#     "Name" : ["Banti", "Sumit", "Robin"],
#     "attr" : [23, 25, 67],
#     "Email" : ["bantihero@gmail.com", "sumit92329@yahoo.com", "robinhood@gmial.com"]
# }
# df = pd.DataFrame(data)
# a = df["Email"].str.split("@")
# print(a)
# print(df)

# data = {
#     "Name" : ["Banti", "Sumit", "Robin"],
#     "Age" : [26, 15, 87],
#     "attr" : [23, 25, 67],
#     "Email" : ["bantihero@gmail.com", "sumit92329@yahoo.com", "robinhood@gmial.com"]
# }
# df = pd.DataFrame(data)
# df["Age Group"] = df["Age"].apply(lambda x: "Adult" if x >= 18 else "Minor")
# df.sort_values(["Age", "attr"], inplace=True)
# df.reset_index(drop=True, inplace=True)
# df["Rank"] = df["Age"].rank() 
# print(df)

# data = {
# 'Name': ['Alice', 'Bob', 'Charlie'],
# 'Math': [85, 78, 92],
# 'Science': [90, 82, 89],
# 'English': [88, 85, 94]
# }
# df = pd.DataFrame(data)


# df = df.melt(id_vars=["Name"], value_vars=["Math", "Science", "English"], var_name="Subject", value_name="Score")
# print(df)

df = pd.DataFrame({
"Department": ["HR", "HR", "IT", "IT", "Marketing", "Marketing", "Sales", "Sales"],
"Team": ["A", "A", "B", "B", "C", "C", "D", "D"],
"Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
"Salary": [85, 90, 78, 85, 92, 88, 75, 80],
"Age": [23, 25, 30, 22, 28, 26, 21, 27],
"JoinDate": pd.to_datetime([
"2020-01-10", "2020-02-15", "2021-03-20", "2021-04-10",
"2020-05-30", "2020-06-25", "2021-07-15", "2021-08-01"
])
})
df = df.groupby("Department")["Salary"].mean()
print(df)