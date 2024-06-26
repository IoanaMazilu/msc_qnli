travel_time_premise = 44
travel_time_hypothesis = 14
average_speed_premise = 50
average_speed_hypothesis = 50

# the hypothesis talks about the travel time and average speed of a bus, referenced also in the premise
if average_speed_hypothesis!= average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
elif travel_time_hypothesis!= travel_time_premise:
    # check if the travel time in the hypothesis contradicts the travel time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
