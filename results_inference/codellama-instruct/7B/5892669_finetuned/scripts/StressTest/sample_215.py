average_speed_premise = 36
average_speed_hypothesis = 36

# the hypothesis refers to the average speed of the whole journey mentioned in the premise
if average_speed_hypothesis >= average_speed_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
