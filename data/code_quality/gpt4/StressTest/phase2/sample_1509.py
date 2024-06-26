stretch_time_premise = 27
stretch_time_hypothesis = 57

# the hypothesis refers to the stretching time of Cathy mentioned in the premise
if stretch_time_hypothesis <= stretch_time_premise:
    # check if the hypothesis value contradicts the given stretching time of Cathy in the premise
    label = "contradiction"
elif stretch_time_hypothesis > stretch_time_premise:
    # the premise gives an exact time for Cathy's stretch
    # any stretch time less than 'stretch_time_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
