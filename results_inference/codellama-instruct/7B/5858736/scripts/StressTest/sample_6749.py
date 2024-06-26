butter_kg_premise = 44
butter_kg_hypothesis = 44

# the hypothesis refers to the number of kg of butter mixed by Raman
if butter_kg_hypothesis <= butter_kg_premise:
    # check if the estimate of 'butter_kg_hypothesis' contradicts the number of kg of butter mixed by Raman
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of kg of butter mixed by Raman
    # any number of kg greater than 'butter_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
