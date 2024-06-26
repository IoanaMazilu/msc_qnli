total_pets_premise = 96
total_pets_hypothesis = 66

# the hypothesis refers to the total number of pets Claire has, which is also mentioned in the premise
if total_pets_hypothesis!= total_pets_premise:
    # check if the number of pets in the hypothesis contradicts the number of pets in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
