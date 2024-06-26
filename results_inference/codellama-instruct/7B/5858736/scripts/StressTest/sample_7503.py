pat_stretch_premise = 10
pat_stretch_hypothesis = 20

if pat_stretch_hypothesis <= pat_stretch_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
