    **Ideas and Tasks**
**Time Schedule-->** https://docs.google.com/spreadsheets/d/1NPq_5cuFRDThXJXZ4-JIx_16YuWSKhH_ok0S__H6rzw/edit?usp=drivesdk

**DSA Course Understanding-->** https://docs.google.com/document/d/1n3MJ73W4vFIdFtSQDgg9vM-K0-OHlW8i/edit?usp=drivesdk&ouid=110502976003929694656&rtpof=true&sd=true

**Daily Understandings-->** https://docs.google.com/document/d/1f9uqDu70LrBFUKJpA8IQM74SRTVeqixq/edit?usp=drivesdk&ouid=110502976003929694656&rtpof=true&sd=true

VDD--> https://docs.google.com/spreadsheets/d/e/2PACX-1vRxRfVUILLq1Ei6hhBGpNr2ERhRpJaZRjLIvN1swPsXP37w6dZA7euDOkPuzjaguCUwrrP8oTZxQBbL/pubhtml

FDD--> https://docs.google.com/spreadsheets/d/e/2PACX-1vRpnjuoGMsQDYyTX2zt5HLndMwitL7UlWaIIDWDVBn5LXPPtqjjGfqbFO25qXi6X112obhGgkNbHKAz/pubhtml

**change the --> pub?output=ods** | xlsx | pdf | csv

FDD Form--> https://docs.google.com/forms/d/e/1FAIpQLSdGKeHsVynj132eEq49Myjb09ZdyPXKCsSN5s2iKYFENODPcg/viewform

VDD Form--> https://docs.google.com/forms/d/e/1FAIpQLSca6Ok8MQcxZNkPp0EDLdhxe9c-X8p5Gm5pXJRyq0TbXdZTwQ/viewform

**NOT DONE**

In **pandas_dataframe_timeslots.py**

**Disclaimer 1-->** Ask for time slots and ask 7 or till user
did not want to stop using while or for loop, whichever suits you.

**Disclaimer 2-->** Make this data printed as a schedule.csv or xlsx as schedule 1, Schedule 2 or Date 1, Date 2 (Learn Read and write to the file using python)

**Disclaimer 3-->** Use the append method to store N number of time slots and also to update and delete use the list.

**Disclaimer 3-->** As soon as you have typed all your Slots, Display it also. So, 1 `<sup>`st `</sup>` Table for Time Slot display & 2 `<sup>`nd `</sup>` for Full Schedule Display.

**Disclaimer 4-->** Make def functions for **ias={tslots,full_schedule,update:(tslots,dt(defined tasks)),delete-a slot (dt_data.drop(tslotslist[user_input_S.No-1]),rename}** and then the name of the def function in the dictionary and ask the user, if the user wanted to add the timeslots, defined tasks, reminders|Help. Then call the action taken by the user as ias[update], ias[full_schedule]

**1-->**  df = df.rename(columns={'A': 'X', 'B': 'Y'}) or| df.rename(columns={'A': 'X'}, index={'X': 'W'}, inplace=True) or| df.index.name = 'Index_Name'

1--> Use User input to ask for **Time Slots** as t1,t2,t3... t7 or user input until user want's to stop

2--> Same as above, ask user to enter the **Defined Tasks** as d1,d2,d3... same number as **Time Slots**

3--> Same goes with **Reminders** as r1,r2... same number as **Time Slots**

4--> Use data_dict={"Time Slots":[t1,t2,t3,...],"Defined Tasks":[d1,d2,d3....],"Reminders":[r1,r2,r3....]}

**Second Normal approach** --> Typing in the schedule simply to the dictionary

**FINAL APPROACH-->**

- [X] An Empty list to ask for timeslots, append the time slot in it.
- [X] For the Defined Tasks, append("Update it..") | then Display the Table with the dict data.
- [X] Two new list for storing Defined Tasks and Help for that. Ask it using a loop as number of times as the number of timeslots (len(timeslots))
- [X] Display, listname means using list name and not the values, display the full schedule.
- [X] Make a new function, (update_full_schedule).
- [ ] Make all the functions for (Add|Delete|)
- [ ] Make Choices with the fucntions name.
- [ ] Make a major choice which asks for the New Schedule & Update current Schedule.
- [ ] Add date time for the file to save with.
- [ ] Keep all the current Schedules and while updating Two options (Update to the same Sheet:Same name will help | New Sheet:New Name will help)
- [ ] Try .csv or .xlsx file to access or to update DataFrames into the .csv file, so to access it later. (If not getting the options to Save New & Update the Current file)
- [ ] Read thge existing schedule with the name of the file and the sheet name, and ask the time slot of reaching back to room and change the schedule time slot with the same Defined tasks using loops to add the time according to the previous existing schedule.

---

**NOT DONE**

In **A New File of Python**

use the CSV or xlsx file to retrieve the data from it and use it in python using the pandas **DataFrame** or any other library. maybe this is in the **Python TuteDude course**

---

**NOT DONE**

Get the wifi names and the passwords for all the wifi connected to the laptop using python

---

**NOT DONE**

get your **ideas_while_work.md** file copy paste in your **JFoldknewme.docx** file saved in Drive and see what happens.

---

**NOT DONE** Tasks of the DAY **(16/11/2024)**
You can sometimes directly copy paste from **ideas_or_tasks.md**

1. **DONE** Gather all your sources, that you access and work on. Make a **Linked Diagram** all. -stored PW -Daily Understanding docs -Programs saved -physical memory -Online memory -Git Memory(**Nikhilgulati841**) --Git Repositories for testing & Completed Projects | Programs (**_PyWhileWork_** & **JFoldknewme**) --daily ideas or tasks while Work(**ideasortasks_while_work.md**) *[Daily Understanding.docx & a Git file daily_understanding.md]*  In short, you have automated your task and include Mess Time Table also.  (0.5 hrs)
2. Work | Revise | Write the concepts of **FDD** and the changes needed (includes **study** Points & Display Daily Learnings in one individual Sheet) (1.5 hrs)
3. Work | Revise | Write on **VDD** (1 hrs)
4. Complete **pandas_dataframe_timeslots.py** (2.5 hrs)
5. **Revision** of all you have done. (1 hrs)
6. Name your APP for pandas_dataframe_timeslots.py (**IAS**--> Implement Analyzed Schedule) **IAS.exe**

---
