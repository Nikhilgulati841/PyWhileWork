#understandings... 
# a=[]
# a.append({"t1":"hello"})
# print(a[0]["t1"])
#understandings...
# a="@3:45 Am book rapido to Room,reach Room @4:10 Am"
# b=a.split(",")
# for i in b:
#     print(i)



from openpyxl import Workbook, load_workbook
import pandas as pd
import datetime 
import os


# a=datetime.now()
# print(a)


#ask for the time slots till the user wanted to
# print("""\nFor the spare time, If you do the task in less time.
# Remember Not to rest | As the TIME LEFT is the TIME you GAINED.
# So, Either do the Next Task or Increase your Productivity.
# Study | Take Break | Meditate | Pull-ups | Push-ups""")
# print("===================================================\n")
print("""Type--> New | To Enter new Schedule Type.
Type--> Update | To update the current Schedule.
Type--> Delete | To delete a Time Slot from current Schedule
Type--> Add    | To add a Time Slot to current Schedule.\n""")




def tslots():
    global tslotlist
    global dtlist
    global tslots
    tslotlist=[]
    dtlist=[] #list just to give an input(update it.. in the Defined Tasks)
    t="a"
    print("Start Entering Time Slots..:\n")
    print("Type--> Stop | Stop taking anymore slots.")
    for i in range(1,31):
        t=input(f"Enter Slot {i}: ")
        if t.lower()!="stop":
            tslotlist.append(t)
            dtlist.append("Update it..")

        elif t.lower()=="stop":
            break

    # print(timelist)

    #use the same list timelist as the list that needs to be provided under column "Slots"
    #this way you will not have to provide all t1,t2,t3,t... till the number of time slots it will ask from the user
    #by this you avoid using another for or while loop to enter n number of t...(n)
    tslots_dict={"T-Slots":tslotlist,"Define Tasks":dtlist
        
    }
    
    tslots=pd.DataFrame(tslots_dict)
    tslots.index=tslots.index+1
    tslots.index.name="S.No"
    # tslots.index.name="Slot Count"  # to update index name
    print("\nTime Slots Displaying...!!\n",tslots)
    print("\n")    
    # print(tslotlist)



def full_schedule():
    #Now asking for the TASKS for each T-Slots
    global dt_dict
    global dtdata
    dt="a"
    help_list=[]  #instead of Dictionary USED List for updating Defined Tasks and Help
    for i in range(len(tslotlist)):  #make tslotslist & dtlist etc.. global to access that variable inside any of the function 
        dt=input(f"Enter Defined Task - [@{tslotlist[i]}]: ")   #dt=> dtlist.keys() as Defined Tasks
        reminder_help=input(f"Enter Help - [@{tslotlist[i]}] for [{dt}]]: ") #help_reminder=> dtlist.values() as **
        dtlist[i]=dt
        help_list.append(reminder_help)
        # help_list[i]=reminder_help
    # print(dtlist)
        
    dt_dict={"T-Slots":tslotlist,"***Defined Tasks***":dtlist,"***HELP***":help_list  
             #when USE Dictionary as dtlist={} then ***Defined Task***:dtlist.keys() & ***Help***:dtlist.values()
        
    }
    
    dtdata=pd.DataFrame(dt_dict)
    dtdata.index+=1
    dtdata.index.name="S.No"
    print("\n")
    print("Schedule Displaying...!!")
    print(dtdata)

    # Define the folder where you want to save the file
    folder_path = 'schedule'

    # Create the directory if it does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Define the full path for the Excel file
    file_path = os.path.join(folder_path, 'NewSchedule(Date).xlsx')

    sheet_name = f"Data_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Ensuring to append without overwriting existing sheets
    

    print(f"DataFrame has been written to {file_path}")

    # dtdata.to_excel('\New Schedule(22/11/2024).xlsx', index=True)   #output.xlsx for the same file to update it
    #output2.xlsx or updated(date).xlsx for the new file for the updated one. 
    #updating existing and a new file

def update_full_schedule():
    while True:    
        t=input("\nEnter, which T-Slot to update: ")
        if t.lower() in tslotlist:
            dt=input("\nEnter Defined Task that : ")
            dtlist[tslotlist.index(t.lower())]=dt
            
        elif t.lower() not in tslotlist:
            print(f"[{t}] T-slot is not there..Please choose the slots present")
            print("\nType Stop to stop taking updates.")
            print(f"***Please check the Schedule***\n {pd.DataFrame(dt_dict)}")
        
        if t.lower()=="stop":
            print("Updates Stopped")
            break
    
    dtdata=pd.DataFrame(dt_dict)
    dtdata.index+=1
    dtdata.index.name="S.No"
    print("\n")
    print("Schedule Displaying...!!")
    print(dtdata)
    folder_path = 'schedule'

    # Create the directory if it does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Define the full path for the Excel file
    file_path = os.path.join(folder_path, 'NewSchedule(Date).xlsx')

    # Save the DataFrame to the specified Excel file
    dtdata.to_excel(file_path, sheet_name='Date3', index=True)

    print(f"DataFrame has been written to {file_path}")
    

# print(dtlist)


#changes from local to remote
#changes from remote to repo and then to pulled local(Nikhil)
#changes from remote to repo and then to pulled local(main)
#changes from remote to repo and then to pulled local

    
tslots()
full_schedule() 

update_full_schedule()





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

# print(data)

# # # b=datetime.now()
# # # print(b)


"""--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------"""

# Two versions for understanding  14/11/2024

# import pandas as pd

# data_dict={"Blocked Time":["@4:30 Am","@10:30 Am","@11:30 Am"],"Tasks to do":["Sleep @4:30 Am","Wake up @10:30 Am","Exercise & bath ^11:30 Am"]}

# data=pd.DataFrame(data_dict,columns=["Blocked Time","Tasks to do"])

# print(data)
# print("\n")
# data=data.set_index("Blocked Time")
# print(data)

# # data=data.drop("@4:30 Am")
# print(data)

# # ----------------------------------------------------------------

# import pandas as pd

# data_dict={"Tasks to do":["Sleep @4:30 Am","Wake up @10:30 Am","Exercise & bath ^11:30 Am"]}

# data=pd.DataFrame(data_dict,columns=["Tasks to do"],index=["@4:30 Am","@10:30 Am","@11:30 Am"])

# print(data)
# # to delete one row, that row should be a index row
# # Also, find the syntax to delete the Column
# data=data.drop("@4:30 Am")
# print(data)
