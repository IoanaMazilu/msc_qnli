percentage_travel_premise = 80
percentage_travel_hypothesis = 50
average_speed_premise = 80
average_speed_hypothesis = 80

# the hypothesis refers to the percentage of travel and average speed mentioned in the premise
if percentage_travel_premise < percentage_travel_hypothesis:
    # check if the percentage of 'percentage_travel_hypothesis' contradicts the percentage of travel in the premise
    label = "contradiction"
elif average_speed_hypothesis != average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
