running_time_premise = 38
running_time_hypothesis = 68

# the hypothesis refers to the time Dawson took to run the first leg of the course mentioned in the premise
if running_time_hypothesis == running_time_premise:
    # check if the hypothesis value contradicts the time reported in the premise
    label = "contradiction"
else:
    # any time greater than 'running_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
