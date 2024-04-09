trip_home_premise = 1.5 # 1/2 hour longer than the trip to the beach
trip_beach_premise = 2 # 2 hours

# the hypothesis refers to the duration of the trip home
if trip_home_premise <= trip_beach_premise:
    # check if the estimate of 'trip_home_premise' contradicts the duration of the trip to the beach
    label = "contradiction"
elif trip_home_premise > 3*trip_beach_premise:
    # check if the duration of the trip home is greater than 3 times the duration of the trip to the beach
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of the trip home
    # any duration less than or equal to 3 times the duration of the trip to the beach is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
