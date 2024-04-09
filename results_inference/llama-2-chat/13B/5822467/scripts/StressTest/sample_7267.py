bruce_bhishma_premise = 200
bruce_bhishma_hypothesis = 600

# the hypothesis refers to the length of the circular track
if bruce_bhishma_hypothesis > bruce_bhishma_premise:
    # check if the hypothesis value contradicts the estimate of 'bruce_bhishma_premise'
    label = "contradiction"
elif bruce_bhishma_hypothesis == bruce_bhishma_premise:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the length of the circular track
    # any length greater than 'bruce_bhishma_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
