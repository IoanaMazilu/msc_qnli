bruce_bhishma_premise = 600
bruce_bhishma_hypothesis = 500

# the hypothesis refers to the length of the circular track
if bruce_bhishma_hypothesis <= bruce_bhishma_premise:
    # check if the hypothesis value contradicts the estimate of the length of the circular track in the premise
    label = "contradiction"
elif bruce_bhishma_hypothesis > bruce_bhishma_premise:
    # check if the hypothesis value entails the estimate of the length of the circular track in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the length of the circular track
    # any length of the circular track greater than or equal to 500 m is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
