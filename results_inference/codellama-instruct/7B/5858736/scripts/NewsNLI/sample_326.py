sailors_premise = 15
sailors_hypothesis = 15
vessels_premise = 2
vessels_hypothesis = 2

if sailors_hypothesis!= sailors_premise:
    label = "contradiction"
elif vessels_hypothesis!= vessels_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
