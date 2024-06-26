butter_kg_premise = 44
butter_kg_hypothesis = 84

if butter_kg_hypothesis >= butter_kg_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
