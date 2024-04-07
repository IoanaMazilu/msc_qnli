# Premise: After less than 40 minutes, Jim stops to stretch.
# Hypothesis: After 30 minutes, Jim stops to stretch.
# Golden Label: neutral

minutes_premise = 40
minutes_hypothesis = 30

# the hypothesis specifies a time when Jim stops to stretch, which is also referenced in the premise
if minutes_hypothesis >= minutes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'minutes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time when Jim stops
    # any time less than 'minutes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

