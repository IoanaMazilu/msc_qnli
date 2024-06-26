butter_kg_premise = 27
butter_kg_hypothesis = 47

if butter_kg_hypothesis <= butter_kg_premise:
    # check if the hypothesis value contradicts the exact amount of butter mixed in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount of butter, any amount greater than 'butter_kg_premise' contradicts the premise
    label = "contradiction"

print(label)
