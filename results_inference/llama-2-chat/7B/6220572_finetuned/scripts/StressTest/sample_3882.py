jog_time_premise = 3
jog_time_hypothesis = 4

# the hypothesis refers to the total jogging and walking time in the premise
if jog_time_hypothesis >= jog_time_premise:
    # check if the hypothesis value contradicts the total jogging and walking time in the premise
    label = "contradiction"
else:
    # any number of hours less than 'jog_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
