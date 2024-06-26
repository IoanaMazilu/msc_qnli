stretch_time_premise = 18
stretch_time_hypothesis = 78

# the hypothesis refers to the time Jim needs to stretch, mentioned also in the premise
if stretch_time_hypothesis <= stretch_time_premise:
    # check if the hypothesis value contradicts the time Jim needs to stretch in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Jim needs to stretch
    # any time greater than'stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
