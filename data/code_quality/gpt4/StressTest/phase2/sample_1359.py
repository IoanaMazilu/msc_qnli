travel_percentage_premise = 80
travel_percentage_hypothesis = 10
average_speed_premise = 80
average_speed_hypothesis = 80

# the hypothesis refers to the percentage and speed of John's travel mentioned in the premise
if travel_percentage_premise <= travel_percentage_hypothesis:
    # check if the estimate of 'travel_percentage_hypothesis' contradicts the percentage of travel in the premise
    label = "contradiction"
elif average_speed_hypothesis != average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
