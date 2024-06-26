butter_kg_premise = 27
butter_kg_hypothesis = 77

if butter_kg_hypothesis!= butter_kg_premise:
    # check if the number of kg of butter in the hypothesis contradicts the number of kg of butter reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
