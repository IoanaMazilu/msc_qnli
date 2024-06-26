average_speed_premise = 43
average_speed_hypothesis = 43

# the hypothesis refers to the average speed from X to Y mentioned in the premise
if average_speed_hypothesis >= average_speed_premise:
    # check if the hypothesis value contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
