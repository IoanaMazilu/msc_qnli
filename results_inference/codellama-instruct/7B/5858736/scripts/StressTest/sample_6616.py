stations_hypothesis = 18
stations_premise = 28

if stations_hypothesis >= stations_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
