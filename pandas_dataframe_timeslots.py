# a="@3:45 Am book rapido to Room,reach Room @4:10 Am"
# b=a.split(",")
# for i in b:
#     print(i)


import pandas as pd

data_dict={"T Slots":["@4:30 Am","@10:30 Am","@11:30 Am"]

data=pd.DataFrame(data_dict,columns=["T Slots","Tasks"])

data=data.set_index("T Slots")
Print(data)
