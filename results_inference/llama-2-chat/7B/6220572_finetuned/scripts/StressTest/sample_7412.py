butter_kg_premise = 27
butter_kg_hypothesis = 77

# the hypothesis refers to the weight of butter mixed by Raman, also mentioned in the premise
if butter_kg_hypothesis <= butter_kg_premise:
    # check if the hypothesis value contradicts the weight of butter in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of butter
    # any weight of butter greater than 'butter_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
