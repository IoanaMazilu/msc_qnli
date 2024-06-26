travel_premise = 7
travel_hypothesis = 4

# the hypothesis talks about the time it takes to travel from A to B and return by cycle, referenced also in the premise
if travel_hypothesis <= travel_premise:
    # check if the hypothesis value contradicts the estimate of more than 'travel_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes to travel by cycle
    # any time greater than 'travel_premise' hours is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
