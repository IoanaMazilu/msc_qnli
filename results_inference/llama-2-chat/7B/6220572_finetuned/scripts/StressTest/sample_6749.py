butter_kg_premise = 44
butter_kg_hypothesis = 44

# the hypothesis talks about the weight of butter mixed, referenced also in the premise
if butter_kg_hypothesis!= butter_kg_premise:
    # check if the hypothesis value contradicts the weight of butter in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of butter
    # any weight of butter greater than 'butter_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
