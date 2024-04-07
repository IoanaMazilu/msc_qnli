# Premise: After less than 20 minutes, Pat stops to stretch.
# Hypothesis: After 10 minutes, Pat stops to stretch.
# Golden Label: neutral

stretch_time_premise = 20
stretch_time_hypothesis = 10

# the hypothesis talks about the time when Pat stops to stretch, which is also referenced in the premise
if stretch_time_hypothesis >= stretch_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'stretch_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time when Pat stops
    # any time less than 'stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
