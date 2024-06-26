average_speed_premise = 80
average_speed_hypothesis = 60
average_speed_return_premise = 70
average_speed_return_hypothesis = 70

# the hypothesis refers to the average speed of the trip and the return trip mentioned in the premise
if average_speed_hypothesis!= average_speed_premise:
    # check if the estimated average speed of the hypothesis contradicts the average speed in the premise
    label = "contradiction"
elif average_speed_return_hypothesis!= average_speed_return_premise:
    # check if the average speed of the return trip in the hypothesis contradicts the average speed of the return trip reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
