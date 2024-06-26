average_shirts_premise = 40
average_shirts_hypothesis = 40

# the hypothesis refers to the average number of shirts mentioned in the premise
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the hypothesis value contradicts the average number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
