percentage_travel_premise = 50
percentage_travel_hypothesis = 80
average_speed_premise = 80
average_speed_hypothesis = 80

# the hypothesis refers to the percentage of the travel and the average speed of John's travel mentioned in the premise
if average_speed_premise != average_speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif percentage_travel_hypothesis <= percentage_travel_premise:
    # check if the 'percentage_travel_hypothesis' contradicts the estimate of more than 'percentage_travel_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the trip
    # any percentage of the trip greater than 'percentage_travel_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
