stations_hypothesis = 15
stations_premise = 75

if stations_hypothesis >= stations_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
