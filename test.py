import datetime
l=[]
dt=[]
for i  in range(5):
    a=input(f"Enter the Date {i}: ")
    task=input(f"Enter the task for timeslot [{a}]")
    b=datetime.datetime.strptime(a,"%I:%M %p").time()
    l.append(b)
    l.sort()
    
a1=input("Enter new timeslot: ")
b1=datetime.datetime.strptime(a1,"%I:%M %p").time()
l.append(b1)
l.sort()
task1=input("Enter the task for new timeslot entered: ")





print("soted list",[i.strftime("%I:%M %p") for i in l])
print(dt)
print(l)