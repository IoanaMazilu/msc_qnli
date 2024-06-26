gang_premise = 5
gang_hypothesis = 5

# the hypothesis refers to the number of gangs Mala has, as mentioned in the premise
if gang_hypothesis <= gang_premise:
    # check if the estimate of 'gang_hypothesis' contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
