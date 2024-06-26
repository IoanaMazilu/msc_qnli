speed_premise = 60
speed_hypothesis = 50

if speed_hypothesis >= speed_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
