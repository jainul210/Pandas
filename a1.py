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

data = {
    "Name" : ["Banti", "Sumit", "Robin"],
    "Age" : [26, 15, 87],
    "attr" : [23, 25, 67],
    "Email" : ["bantihero@gmail.com", "sumit92329@yahoo.com", "robinhood@gmial.com"]
}
df = pd.DataFrame(data)
df["Age Group"] = df["Age"].apply(lambda x: "Adult" if x >= 18 else "Minor")
print(df)