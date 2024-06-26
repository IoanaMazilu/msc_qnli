stations_premise = 85
stations_hypothesis = 25

# check if the hypothesis value contradicts the estimate of'stations_premise'
if stations_hypothesis <= stations_premise:
    label = "contradiction"
elif stations_hypothesis > stations_premise:
    # the hypothesis value is greater than the estimate in the premise, so entailment
    label = "entailment"
else:
    # if the hypothesis value is equal to the estimate in the premise, then neutral
    label = "neutral"

print(label)
