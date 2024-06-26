travel_time_premise = 24 #in minutes
travel_time_hypothesis = 44 #in minutes
average_speed_premise = 50 #in km/hr
average_speed_hypothesis = 50 #in km/hr

# the hypothesis refers to the travel time and average speed mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the 'travel_time_hypothesis' contradicts the estimate of more than 'travel_time_premise' minutes
    label = "contradiction"
elif average_speed_hypothesis != average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # the premise provides an estimate for the travel time and a specific average speed
    # any travel time greater than 'travel_time_premise' and the same average speed is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
