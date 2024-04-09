bruce_bhishma_premise = 600
bruce_bhishma_hypothesis = 200

# the hypothesis refers to the length of the circular track
if bruce_bhishma_hypothesis > bruce_bhishma_premise:
    # the hypothesis explicitly entails the premise
    label = "entailment"
elif bruce_bhishma_hypothesis <= bruce_bhishma_premise:
    # the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis contradicts the premise
    label = "contradiction"

print(label)
