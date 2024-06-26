travel_time_premise = 44
travel_time_hypothesis = 14
average_speed_premise = 50
average_speed_hypothesis = 50

# the hypothesis refers to the travel time and average speed of the bus mentioned in the premise
if travel_time_premise!= travel_time_hypothesis:
    # check if the travel time in the hypothesis contradicts the travel time reported in the premise
    label = "contradiction"
elif average_speed_premise!= average_speed_hypothesis:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
