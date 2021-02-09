# This program will ask for the runners speed in mph
# and then calculate the amount of time in hours and
# minutes it will take the runner to complete the task.

# Obtain the speed of the runner.
speedStr = input("Your constant speed(mph): ")
SPEED_OF_RUNNER = int(speedStr)

# Compute and print the mile times for the runner
# Time into minutes is the formula: time = (distance/speed)*60

Five_mile = (5/SPEED_OF_RUNNER)*60 # This turns the the 5 miles into minutes
Minutes = int(Five_mile)     # Assigning the 5 miles to minutes variable
Hours = int(Five_mile/60)    # divides the number of minutes into hours
print("You will run 5 miles for " + str(Hours) + " hour(s) and " + str(Minutes) + " minute(s),")


Ten_mile = (10/SPEED_OF_RUNNER)*60  # This will turn the 10 miles into minutes
Minutes = int(Ten_mile)     # Assigning the 10 miles to minutes variable
Hours = int(Ten_mile/60)    # divides the number of minutes into hours
print("10 miles for " + str(Hours) + " hour(s) and " + str(Minutes) + " minute(s),")

Half_mara = (13.1/SPEED_OF_RUNNER)*60   # This turns a half marathon into minutes
Minutes = int(Half_mara)     # Assigning the half marathon to minutes variable
Hours = int(Half_mara/60)    # divides the number of minutes into hours
print("a half marathon miles for " + str(Hours) + " hour(s) and " + str(Minutes) + " minute(s),")


Full_mara = (26.2/SPEED_OF_RUNNER)*60 # This turns a full marathon into minutes
Minutes = int(Full_mara)     # Assigning the full marathon to minutes variable
Hours = int(Full_mara/60)    # divides the number of minutes into hours
print("and a full marathon for " + str(Hours) + " hour(s) and " + str(Minutes) + " minute(s).")
