butter_kg_premise = 44
butter_kg_hypothesis = 44

# the hypothesis refers to the amount of butter mentioned in the premise
if butter_kg_hypothesis <= butter_kg_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact amount of butter, 
    # any amount of butter greater than 'butter_kg_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
