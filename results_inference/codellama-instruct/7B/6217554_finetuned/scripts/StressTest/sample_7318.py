stretch_time_premise = 78
stretch_time_hypothesis = 18

# the hypothesis talks about the time Jim needs to stretch, referenced also in the premise
if stretch_time_hypothesis >= stretch_time_premise:
    # check if the time Jim needs to stretch in the hypothesis contradicts the estimate of less than'stretch_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Jim needs to stretch
    # any time less than'stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
