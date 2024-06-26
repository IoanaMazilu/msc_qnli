butter_kg_premise = 44
butter_kg_hypothesis = 44

if butter_kg_hypothesis!= butter_kg_premise:
    # check if the number of butter in the hypothesis contradicts the number of butter reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
