T_premise = 20
T_hypothesis = 20

# the hypothesis refers to the value of T mentioned in the premise
if T_hypothesis >= T_premise:
    # check if the hypothesis value contradicts the premise statement of T being less than T
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
