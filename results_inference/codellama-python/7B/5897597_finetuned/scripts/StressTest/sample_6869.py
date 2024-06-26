people_premise = 5
people_hypothesis = 5

# the hypothesis refers to the number of people that can be seated on a bench, also mentioned in the premise
if people_hypothesis <= people_premise:
    # check if the hypothesis value contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
