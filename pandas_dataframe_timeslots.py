#understandings...
# a=[]
# a.append({"t1":"hello"})
# print(a[0]["t1"])
#understandings...
# a="@3:45 Am book rapido to Room,reach Room @4:10 Am"
# b=a.split(",")
# for i in b:
#     print(i)


import pandas as pd
from datetime import datetime 

# a=datetime.now()
# print(a)

timelist=[]
t=0
#ask for the time slots till the user wanted to
print("""Enter the time slots(as many as you want), 
and when you wish to stop..!! taking anymore slots| **Type--> ok in Small Letters**\n""")

for i in range(1,21):
    if t!="ok":
        t=input(f"Enter Slot {i}:")
        timelist.append(t)
    elif t=="ok" or t=="Ok" or t=="OK":
        timelist.remove(timelist[-1])
        break
        
# print(timelist)

#use the same list timelist as the list that needs to be provided under column "Slots"
#this way you will not have to provide all t1,t2,t3,t... till the number of time slots it will ask from the user
#by this you avoid using another for or while loop to enter n number of t...(n)
dict_tslots={"T-Slots":timelist
    
}

tslots=pd.DataFrame(dict_tslots)
tslots.index=tslots.index+1
tslots.index.name="S.No"
# tslots.index.name="Slot Count"  # to update index name
print("\nTime Slots Displaying...!!\n",tslots)


# data_dict={"T-Slots":["@4:10 Am","@4:30 Am","@10:00 Am","@11:00 Am","@12:00 Pm",
# "@5:00 Pm","@5:40 Pm","@6:00 Pm","@6:20 Pm","@7:45 Pm","@10:45 Pm","@1:30 Am","@3:45 Am"],

# "DEFINED TASKS          ":["Reached Room","Start Studying","Study till here","Revision Time",
#                         "Exercise|bath|1st Meal|Sleep","Sleep Till here","Ready for Office",
#                         "Office Ride Book","Office On Time","Eat Protien full food",
#                         "2nd Meal | FDD Filling","Next day Plan","Ride #back to Room"],
                        
#         "REMINDER   ":["NO Distraction","FreshUp|10m BrB","","Mandate",5,6,7,8,9,10,11,12,13],
#         "Need HELP..!!":["No Talking|Smoking","20-Water-Face-Splash",3,"Mandate",5,6,7,8,9,10,11,12,13]}

# data=pd.DataFrame(data_dict) #Other approach--> data=pd.DataFrame(data_dict,column="T-Slots","DEFINED TASKS          ",
# #""... etc like that )
# # data["TASKS"].str.pad(width=4,fillchar="T",side="both")
# data=data.set_index("T-Slots")

# print("""\nFor the spare time, If you do the task in less time.
# Remember Not to rest | As the TIME LEFT is the TIME you GAINED.
# So, Either do the Next Task or Increase your Productivity.
# Take Break | Meditate | Pull-ups | Push-ups""")
# print("===================================================\n")

# print(data)

# # # b=datetime.now()
# # # print(b)
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
