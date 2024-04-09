butter_kg_premise = 44
butter_kg_hypothesis = 84

# the hypothesis refers to the quantity of butter mixed by Raman mentioned in the premise
if butter_kg_premise >= butter_kg_hypothesis:
    # check if the estimate of 'butter_kg_hypothesis' contradicts the quantity of butter in the premise
    label = "contradiction"
elif butter_kg_premise < butter_kg_hypothesis:
    # if the quantity of butter in the premise is less than the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
