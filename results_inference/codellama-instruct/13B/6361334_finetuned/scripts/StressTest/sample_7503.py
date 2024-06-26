time_premise = 10
time_hypothesis = 20

# the hypothesis refers to the time after which Pat stops to stretch, which is also mentioned in the premise
if time_hypothesis >= time_premise:
    # check if the hypothesis value contradicts the time in the premise
    label = "contradiction"
else:
    # the premise gives an exact time after which Pat stops to stretch
    # any time less than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)