gangs_premise = 8
gangs_hypothesis = 3

# the hypothesis refers to the number of gangs mentioned in the premise
if gangs_hypothesis >= gangs_premise:
    # check if the hypothesis value contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
