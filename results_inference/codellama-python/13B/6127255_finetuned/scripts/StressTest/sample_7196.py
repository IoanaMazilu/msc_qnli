time_premise = 7 + 1/24/60
time_hypothesis = 7 + 1/24/60

# the hypothesis refers to the time required by a train to cover the distance between Chennai and Jammu, also mentioned in the premise
if time_hypothesis <= time_premise:
    # check if the hypothesis value contradicts the exact time mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an exact time for the distance
    # any time greater than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
