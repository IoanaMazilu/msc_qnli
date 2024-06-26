people_seated_premise = 5
people_seated_hypothesis = 5

# the hypothesis refers to the number of people seated, which is also mentioned in the premise
if people_seated_hypothesis <= people_seated_premise:
    # check if the number of people seated in the hypothesis contradicts the number of people seated in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
