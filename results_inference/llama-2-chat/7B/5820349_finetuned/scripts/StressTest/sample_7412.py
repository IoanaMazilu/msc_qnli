butter_kg_premise = 27
butter_kg_hypothesis = 77

# the hypothesis refers to the quantity of butter mixed by Raman mentioned in the premise
if butter_kg_premise!= butter_kg_hypothesis:
    # check if the quantity of butter in the hypothesis contradicts the quantity of butter reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
