<h1 align=center>Ideas and Tasks</h1>   


 `-quote` 
<details>
  <summary>Karte ja tu bandeya</summary>
  <br>Karte ja tu bandeya,
  <br>Jab tak teri na ho fateh,
  <br>Na rakh uspe koi shikan,
  <br>chahe ho Fateh, ya Marjaaye karte fateh.<br>
  <br>Chadha le bulandiyon ke nashe,
  <br>rakh hausla Teri hogi fateh,
  <br>fir na rukna kahin tu bin pohoche vahan,
  <br>fir agar rukna hi hai, toh krna mat tum bulandiyon ke nashe,
  <br>pr agr chadh hi Chuka hai suroor junoon ka,
  <br>toh nikal ja lad ja fir tu kar ja fateh.
</details>

## Links

*` private`* &copy; Nikhil Gulati | Do not Modify or Copy any of the below data..!
<details>
  <summary><b>FDD</b></summary>
 
  <br> `web version` pubhtml <br>
   `download version` pub?output=xlsx|ods|pdf|csv|etc...
  <ul>
   <li><a href="https://docs.google.com/spreadsheets/d/1tdlBoFMRnPkawkPP3aBIh_36WWco4yywDFsvKq0L1h4/edit?usp=sharing" target="_blank" rel="noopener noreferrer">View | Edit</a></li>
   <li><a href="https://docs.google.com/forms/d/e/1FAIpQLSdGKeHsVynj132eEq49Myjb09ZdyPXKCsSN5s2iKYFENODPcg/viewform" target="_blank">Fill the form</a></li>
   <li><a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vRpnjuoGMsQDYyTX2zt5HLndMwitL7UlWaIIDWDVBn5LXPPtqjjGfqbFO25qXi6X112obhGgkNbHKAz/pub?output=xlsx" target="_blank">Download it</li>
  </ul>
</details>
<details>
 <summary><b>VDD</b></summary>
 
 <br> `web version` pubhtml<br>
 `download version` pub?output=xlsx|ods|pdf|csv|etc...
  <ul>
  <li><a href="https://docs.google.com/spreadsheets/d/1NPq_5cuFRDThXJXZ4-JIx_16YuWSKhH_ok0S__H6rzw/edit?usp=drivesdk" target="_blank">View | Edit</a></li>
  <li><a href="https://docs.google.com/forms/d/e/1FAIpQLSca6Ok8MQcxZNkPp0EDLdhxe9c-X8p5Gm5pXJRyq0TbXdZTwQ/viewform" target="_blank">Fill the form</a></li>
  <li><a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vRxRfVUILLq1Ei6hhBGpNr2ERhRpJaZRjLIvN1swPsXP37w6dZA7euDOkPuzjaguCUwrrP8oTZxQBbL/pubhtml" target="_blank">Download it</a></li>
  </ul>
  </p>
</details>
<details>
 <summary><b>Docs</b></summary>
 <ol>
  <li><a href="https://docs.google.com/document/d/1f9uqDu70LrBFUKJpA8IQM74SRTVeqixq/edit?usp=drivesdk&ouid=110502976003929694656&rtpof=true&sd=true" target="_blank">Daily Understandings</a></li>
  <li><a href="https://docs.google.com/document/d/1n3MJ73W4vFIdFtSQDgg9vM-K0-OHlW8i/edit?usp=drivesdk&ouid=110502976003929694656&rtpof=true&sd=true" target="_blank">DSA Course Understandings</a></li>
  <li><a href="https://docs.google.com/document/d/1fae8Oup7dCE64EHe1Q1TdkEQtou7CL0l/edit?usp=drivesdk&ouid=110502976003929694656&rtpof=true&sd=true" target="_blank">DSA & Platforms Practice Problems Understandings</a></li>
  <li><a href="https://docs.google.com/document/d/1fgUV65OIkiZV4YrvbXJ0N9BrCj4vuchg/edit?usp=drivesdk&ouid=110502976003929694656&rtpof=true&sd=true" target="_blank">Python All Understandings</li>
  <li><a href="https://1drv.ms/o/c/73b62c33f0943b59/Elk7lPAzLLYggHOYAQAAAAABS0_A5f9chMMYPpS9KRSOYQ?e=VX7enQ" target="_blank">Draw Notes</a></li>
 </ol>
</details>
   
[comment]: # 


## TimeSlot program
```
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
```
## FINAL APPROACH

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



## To do

In **A New File of Python**

use the CSV or xlsx file to retrieve the data from it and use it in python using the pandas **DataFrame** or any other library. maybe this is in the **Python TuteDude course**

---

## To do

Get the wifi names and the passwords for all the wifi connected to the laptop using python

