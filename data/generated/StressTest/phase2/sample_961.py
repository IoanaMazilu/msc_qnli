# Premise: A runner runs the more than 10 miles from Marathon to Athens at a constant speed.
# Hypothesis: A runner runs the 40 miles from Marathon to Athens at a constant speed.
# Golden Label: neutral

miles_premise = 10
miles_hypothesis = 40

# the hypothesis talks about the distance from Marathon to Athens, mentioned also in the premise
if miles_hypothesis <= miles_premise:
    # check if the hypothesis value contradicts the estimate of more than 'miles_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'miles_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

