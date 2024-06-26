butter_kg_premise = 27
butter_kg_hypothesis = 77

# the hypothesis refers to the amount of butter mixed by Raman mentioned in the premise
if butter_kg_hypothesis!= butter_kg_premise:
    # check if the amount of butter in the hypothesis contradicts the amount of butter mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
