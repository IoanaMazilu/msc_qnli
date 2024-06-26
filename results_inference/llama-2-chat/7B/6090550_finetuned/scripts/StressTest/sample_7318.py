stretch_time_premise = 78
stretch_time_hypothesis = 18

# the hypothesis refers to the time Jim takes to stretch, which is also mentioned in the premise
if stretch_time_hypothesis >= stretch_time_premise:
    # check if the hypothesis value contradicts the premise statement of less than'stretch_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Jim takes to stretch
    # any time less than'stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
