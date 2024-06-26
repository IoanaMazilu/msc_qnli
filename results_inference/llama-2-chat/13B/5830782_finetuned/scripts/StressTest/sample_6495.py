travel_time_premise = 44
travel_time_hypothesis = 24
avg_speed_premise = 50
avg_speed_hypothesis = 50

# the hypothesis refers to the travel time and average speed of a bus mentioned in the premise
if travel_time_premise < travel_time_hypothesis:
    # check if the estimate of 'travel_time_hypothesis' contradicts the travel time in the premise
    label = "contradiction"
elif avg_speed_hypothesis!= avg_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
