average_shirts_premise = 40
average_shirts_hypothesis = 40
purchased_shirts = 8

# the hypothesis refers to the average number of shirts and the number of shirts purchased by each person
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
