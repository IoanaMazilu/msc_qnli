butter_kg_premise = 27
butter_kg_hypothesis = 77

if butter_kg_hypothesis <= butter_kg_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)