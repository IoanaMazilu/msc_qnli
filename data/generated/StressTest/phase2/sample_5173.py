# Premise: After less than 42 minutes, Cathy stops to stretch.
# Hypothesis: After 12 minutes, Cathy stops to stretch.
# Golden Label: neutral

stretch_time_premise = 42
stretch_time_hypothesis = 12

# the hypothesis talks about the time Cathy stops to stretch, referenced also in the premise
if stretch_time_hypothesis >= stretch_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'stretch_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Cathy stops to stretch
    # any time less than 'stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

