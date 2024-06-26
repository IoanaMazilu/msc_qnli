speed_premise = 40
speed_hypothesis = 70

if speed_hypothesis >= speed_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
