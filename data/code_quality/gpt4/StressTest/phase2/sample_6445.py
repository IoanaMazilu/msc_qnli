frank_younger_premise = 84
frank_younger_hypothesis = 14

# the hypothesis refers to the age difference between Frank and John, also mentioned in the premise
if frank_younger_hypothesis > frank_younger_premise:
    # check if the age difference from the hypothesis contradicts the estimate of less than 'frank_younger_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age difference
    # any age difference less than 'frank_younger_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
