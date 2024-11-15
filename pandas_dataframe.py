# Two versions for understanding  14/11/2024

import pandas as pd

data_dict={"Blocked Time":["@4:30 Am","@10:30 Am","@11:30 Am"],"Tasks to do":["Sleep @4:30 Am","Wake up @10:30 Am","Exercise & bath ^11:30 Am"]}

data=pd.DataFrame(data_dict,columns=["Blocked Time","Tasks to do"])

print(data)
print("\n")
data=data.set_index("Blocked Time")
print(data)

# data=data.drop("@4:30 Am")
print(data)

# ----------------------------------------------------------------

import pandas as pd

data_dict={"Tasks to do":["Sleep @4:30 Am","Wake up @10:30 Am","Exercise & bath ^11:30 Am"]}

data=pd.DataFrame(data_dict,columns=["Tasks to do"],index=["@4:30 Am","@10:30 Am","@11:30 Am"])

print(data)
# to delete one row, that row should be a index row
# Also, find the syntax to delete the Column
data=data.drop("@4:30 Am")
print(data)
