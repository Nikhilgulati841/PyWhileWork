# a="@3:45 Am book rapido to Room,reach Room @4:10 Am"
# b=a.split(",")
# for i in b:
#     print(i)


import pandas as pd
from datetime import datetime 

# a=datetime.now()
# print(a)

        

data_dict={"T Slots":["4:10 Am","@4:30 Am","@10:00 Am","@11:00 Am","@12:00 Pm","5:00 Pm","5:40 Pm","6:00 Pm","","7:45 Pm","10:45 Pm","1:30 Am","3:45 Am"],

"DEFINED TASKS          ":["Reached Room, ready for studying",                    "Start Studying","Study till here","Revision Time",
                        "Exercise Buddy, bath & Sleep","Sleep Till here","Ready for Office","Office Ride Book",""],
                        
        "REMINDER   ":["a","b","c","d","e"],"HELP":["a","b","c","d","e"]}

data=pd.DataFrame(data_dict)
# data["TASKS"].str.pad(width=4,fillchar="T",side="both")
data=data.set_index("T Slots")
print(data)

# # b=datetime.now()
# # print(b)

"""--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------"""

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
