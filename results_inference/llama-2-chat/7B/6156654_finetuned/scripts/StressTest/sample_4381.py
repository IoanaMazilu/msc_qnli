# The premise gives the total time Andrew drove from City A to City B,
# as well as the average speed for different sections of the trip.
total_time = 3 + 3
average_speed_premise = 50
average_speed_hypothesis = 60

# The hypothesis gives the time Andrew drove at 50 mph and 60 mph.
time_driven_at_50 = 1
time_driven_at_60 = 3

# The hypothesis also states that Andrew drove for 1 hour at 50 mph.
time_driven_at_50_hypothesis = 1

# The hypothesis cannot be entailed from the premise, as it provides additional information
# about the duration of the drive at different speeds.
label = "neutral"

print(label)
