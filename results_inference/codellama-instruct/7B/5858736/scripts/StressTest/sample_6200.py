stations_hyderabad_bangalore_premise = 18
stations_hyderabad_bangalore_hypothesis = 88

if stations_hyderabad_bangalore_hypothesis <= stations_hyderabad_bangalore_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)