butter_kg_premise = 44
butter_kg_hypothesis = 44

# the hypothesis refers to the amount of butter mixed by Raman, which is also mentioned in the premise
if butter_kg_hypothesis!= butter_kg_premise:
    # check if the amount of butter mixed in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the amount of butter mixed in the hypothesis does not contradict the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
