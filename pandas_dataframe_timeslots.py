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
print(datetime.datetime.now())

def tslots():
    global tslotlist
    global dtlist
    global tslots
    tslotlist=[]
    dtlist=[] #list just to give an input(update it.. in the Defined Tasks)
    t="a"
    print("Start Entering Time Slots in Format[Hour(XX):Minutes(XX) am/pm]:\n")
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
    global help_list
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

   
def update_full_schedule():
    global dtdata
    while True:    
        t=input("\nEnter, which T-Slot to update: ")
        if t.lower() in tslotlist:
            dt=input("\nEnter Defined Task that : ")
            dtlist[tslotlist.index(t.lower())]=dt
            reminder_help=input(f"Enter the Help for [{dt}]: ")
            help_list[tslotlist.index(t.lower())]=reminder_help

            
        elif t.lower() not in tslotlist:
            print(f"[{t}] T-slot is not there..Please choose the slots present")
            print("\nType Stop to stop taking updates.")
            print("***Please check the Schedule***\n")
            print(dtdata)
        
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


def delete():
    global dtdata
    print("\nReview the existing data and select which time slot to delete")
    print(dtdata)
    ask_delete=input("\nEnter the time slot that you wish to delete: ")
    delete=dtdata[dtdata['T-Slots'] != ask_delete]
    print(f"Deleted T-Slot :{ask_delete}\n")
    delete=delete.reset_index(drop=True)
    delete.index+=1
    print(delete)        

def add():
    global tslotlist
    global dtlist
    global help_list
    global dtdata
    
    # Define a helper function to parse time slots into datetime objects
    def parse_time_slot(slot):
        return datetime.datetime.strptime(slot, "%I:%M %p")
    
    print("\nAdd a new time slot with a defined task and reminder.")
    while True:
        new_tslot = input("Enter the new time slot (in format [Hour:Minutes am/pm]): ").strip()
        if new_tslot in tslotlist:
            print(f"The time slot [{new_tslot}] already exists. Please choose a different slot.")
            continue

        new_task = input(f"Enter the defined task for [{new_tslot}]: ").strip()
        new_help = input(f"Enter the reminder for [{new_task}] at [{new_tslot}]: ").strip()

        tslotlist.append(new_tslot)
        dtlist.append(new_task)
        help_list.append(new_help)

        tslotlist=tslotlist()






        # try:
        #     # Ask the user to input the new time slot
        #     new_tslot = input("Enter the new time slot (in format [Hour:Minutes am/pm]): ").strip()
        #     new_tslot_time = parse_time_slot(new_tslot)  # Ensure valid format
            
        #     # Check if the time slot already exists
        #     if new_tslot in tslotlist:
        #         print(f"The time slot [{new_tslot}] already exists. Please choose a different slot.")
        #         continue
            
        #     # Ask for the defined task
        #     new_task = input(f"Enter the defined task for [{new_tslot}]: ").strip()
            
        #     # Ask for the reminder/help
        #     new_help = input(f"Enter the reminder for [{new_task}] at [{new_tslot}]: ").strip()
            
        #     # Add the new time slot, task, and reminder to the lists
        #     tslotlist.append(new_tslot)
        #     dtlist.append(new_task)
        #     help_list.append(new_help)
            
        #     # Parse all time slots into datetime objects
        #     parsed_slots = [parse_time_slot(slot) for slot in tslotlist]
            
        #     # Get the indices of the sorted parsed time slots
        #     sorted_indices = sorted(range(len(parsed_slots)), key=lambda i: parsed_slots[i])
            
        #     # Update the lists in the sorted order
        #     tslotlist = [tslotlist[i] for i in sorted_indices]
        #     dtlist = [dtlist[i] for i in sorted_indices]
        #     help_list = [help_list[i] for i in sorted_indices]
            
        #     # Update the schedule DataFrame
        #     dt_dict = {
        #         "T-Slots": tslotlist,
        #         "***Defined Tasks***": dtlist,
        #         "***HELP***": help_list
        #     }
        #     dtdata = pd.DataFrame(dt_dict)
        #     dtdata.index += 1
        #     dtdata.index.name = "S.No"
            
        #     print("\nUpdated Schedule Displaying...!!")
        #     print(dtdata)
        #     break
        
        # except ValueError:
        #     print("Invalid time format! Please enter the time in [Hour:Minutes am/pm] format.")



    



def save():

    #Define the folder where you want to save the file
    folder_path = 'MySchedule'
    name=input("\n==> Enter the File name to be saved with: ")

    # Create the directory if it does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Define the full path for the Excel file
    file_path = os.path.join(folder_path, f'{name}.xlsx')

    sheet_name = f"Data_{datetime.datetime.now().strftime('%d/%m/%Y_%I:%M:%S %p')}"

    try:
        # Save the DataFrame to the specified Excel file
        dtdata.to_excel(file_path, sheet_name=sheet_name, index=True)
        print(f"DataFrame has been written to {file_path}")

    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
    

# print(dtlist)
#ask for the time slots till the user wanted to
# print("""\nFor the spare time, If you do the task in less time.
# Remember Not to rest | As the TIME LEFT is the TIME you GAINED.
# So, Either do the Next Task or Increase your Productivity.
# Study | Take Break | Meditate | Pull-ups | Push-ups""")
# print("===================================================\n")
print("""Type--> New | To Enter new Schedule Type.
Type--> Update | To update the current Schedule.
Type--> Delete | To delete a Time Slot from current Schedule
Type--> Add    | To add a Time Slot to current Schedule.
Type--> Save   | To Save the Schedule.\n""")


while True:
    choice=input("\nChoose your Choice: ")
    if choice.lower()=="new":
        tslots()
        full_schedule()
    elif choice.lower()=="update":
        update_full_schedule()
    elif choice.lower()=="delete":
        delete()
    elif choice.lower()=="add":
        add()
    elif choice.lower()=="save":
        save()
    elif choice.lower()=="exit":
        print("\nThank you for using MyScheduler App | Application Exitted..")
        break
    else:
        print("This is not an option, please choose among the options..")



    
# tslots()
# full_schedule() 

# update_full_schedule()
# delete()





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
