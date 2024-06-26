average_speed_premise = 36
average_speed_hypothesis = 76

# the hypothesis refers to the average speed of the whole journey mentioned in the premise
if average_speed_premise >= average_speed_hypothesis:
    # check if the estimate of 'average_speed_hypothesis' contradicts the average speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
