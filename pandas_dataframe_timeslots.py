# a="@3:45 Am book rapido to Room,reach Room @4:10 Am"
# b=a.split(",")
# for i in b:
#     print(i)


import pandas as pd

data_dict={"TASKS    ":["Start Studying","Study till here","REVISION","Exercise, bath & Sleep"],"REMINDERS":["a","b","c","d"],"T Slots":["@4:30 Am","@10:30 Am","@11:30 Am","@12:30 Pm"]}

data=pd.DataFrame(data_dict)
# data["TASKS"].str.pad(width=4,fillchar="T",side="both")
data=data.set_index("T Slots")
print(data)
