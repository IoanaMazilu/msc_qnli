average_shirts_premise = 54
average_shirts_hypothesis = 34
purchased_shirts = 8

# the hypothesis refers to the average number of shirts with each person, also mentioned in the premise
if average_shirts_hypothesis != average_shirts_premise:
    # check if the average number of shirts in the hypothesis contradicts the average number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
