butter_kg_premise = 14
butter_kg_hypothesis = 54

# the hypothesis talks about the amount of butter mixed by Raman
if butter_kg_hypothesis <= butter_kg_premise:
    # check if the hypothesis value contradicts the estimate of more than 'butter_kg_premise' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of butter mixed
    # any amount of butter greater than 'butter_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
