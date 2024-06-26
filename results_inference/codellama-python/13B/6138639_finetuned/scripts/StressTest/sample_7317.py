stretch_time_premise = 18
stretch_time_hypothesis = 78

# the hypothesis refers to the time it takes Jim to stretch, which is also mentioned in the premise
if stretch_time_hypothesis <= stretch_time_premise:
    # check if the hypothesis estimate contradicts the time it takes Jim to stretch in the premise
    label = "contradiction"
else:
    # the premise gives an exact time for Jim to stretch
    # any time less than'stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
