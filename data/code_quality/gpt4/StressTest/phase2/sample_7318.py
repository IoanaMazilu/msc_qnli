stretch_time_premise = 78
stretch_time_hypothesis = 18

# The hypothesis refers to the same stretching time mentioned in the premise
if stretch_time_hypothesis >= stretch_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'stretch_time_premise'
    label = "contradiction"
elif stretch_time_hypothesis < stretch_time_premise:
    # any stretching time less than 'stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
