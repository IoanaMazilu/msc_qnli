stretch_time_premise = 38
stretch_time_hypothesis = 18

# the hypothesis refers to the time when Cathy stops to stretch, also mentioned in the premise
if stretch_time_hypothesis >= stretch_time_premise:
    # check if the hypothesis time contradicts the estimate of less than 'stretch_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time when Cathy stops
    # any time less than 'stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
