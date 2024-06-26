butter_kg_premise = 44
butter_kg_hypothesis = 84

# the hypothesis refers to the amount of butter mixed by Raman mentioned in the premise
if butter_kg_premise >= butter_kg_hypothesis:
    # check if the amount of butter in the premise contradicts the estimate of less than 'butter_kg_hypothesis'
    label = "contradiction"
else:
    # if the amount of butter in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
