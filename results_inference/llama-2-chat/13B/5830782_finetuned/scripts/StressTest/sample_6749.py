butter_kg_premise = 44
butter_kg_hypothesis = 44

# the hypothesis refers to the amount of butter mixed by Raman, mentioned in the premise
if butter_kg_hypothesis >= butter_kg_premise:
    # check if the hypothesis value contradicts the exact amount of butter in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
