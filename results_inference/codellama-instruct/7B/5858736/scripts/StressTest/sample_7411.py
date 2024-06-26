butter_kg_premise = 47
butter_kg_hypothesis = 27

if butter_kg_hypothesis <= butter_kg_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
