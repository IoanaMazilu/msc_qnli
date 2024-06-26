 time_premise = 75
time_hypothesis = 75

# the hypothesis refers to the time frame for which Sreedhar can do the work alone, mentioned in the premise
if time_hypothesis >= time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'time_premise'
    label = "contradiction"
elif time_hypothesis < time_premise:
    # the hypothesis value is less than the premise value, so it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, it is not contradictory
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
