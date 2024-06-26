time_premise = 4
time_hypothesis = 7

if time_hypothesis <= time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Kiran takes to travel from A to B and return
    # any time greater than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
