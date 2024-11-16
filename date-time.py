from datetime import datetime, date, time, timedelta
import pytz       #BEGGINING OF 2025, I WILL APPLY FOR PYTHON DEVELOPER JOBS
#Normal Timezone
a=datetime.now()
print(a)
print(f"TimeZone Name: {a.tzinfo}")
print("\n")
#Chnaging timezone
set_timezone=pytz.timezone("Asia/Kolkata")
timeframe=datetime.now(set_timezone)
#Setting the format of the view point of the date you want
b=timeframe.strftime("Weekday: %A\nTime: %I:%M:%S %p\nDate: %d-%b-%Y")
print(b)
#name of the timezones
print(f"TimeZone Name: {timeframe.tzname()}")
print(f"TimeZone: {timeframe.tzinfo}")

print("\n")
add=int(input("How many days to today: "))
print(f"\nAdding...!!| {add} days added to today:\n")
#adding days to the timezone changed recently (timeframe->correct : b->incorrect)
c=timeframe+timedelta(days=add)
print(c.strftime("Weekday: %A\nTime: %I:%M:%S %p\nDate: %d-%b-%Y"))

#Now add days to the date given by the user (strptime)
user_input_date=input("\nEnter the date you wish to get added | Format[day(XX)-month(XX)-year(XXXX)]: ")

user_date=datetime.strptime(user_input_date,"%d-%m-%Y")
print("\n")
print(f"Adding {add} days...!! to this DATE: {user_input_date}\n")
d=user_date+timedelta(days=add)
print(d.strftime("Weekday: %A\nTime: %I:%M:%S %p\nDate: %d-%b-%Y"))

#How to get analyze the timezone oif the given time according to the current printed timings


