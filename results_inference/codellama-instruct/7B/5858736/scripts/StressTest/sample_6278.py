stations_premise = 15
stations_hypothesis = 75

if stations_hypothesis <= stations_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
