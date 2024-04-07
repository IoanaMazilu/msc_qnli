# Premise: If Suresh is 25% more efficient than Kamal, he can complete the work in---days.
# Hypothesis: If Suresh is 15% more efficient than Kamal, he can complete the work in---days.
# Golden Label: contradiction

suresh_efficiency_premise = 25
suresh_efficiency_hypothesis = 15

# the hypothesis talks about Suresh's efficiency in comparison to Kamal, which is also mentioned in the premise
if suresh_efficiency_hypothesis > suresh_efficiency_premise:
    # check if the hypothesis value contradicts the premise value for Suresh's efficiency
    label = "contradiction"
elif suresh_efficiency_hypothesis < suresh_efficiency_premise:
    # the premise provides a higher value for Suresh's efficiency
    # a lower efficiency as in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value for Suresh's efficiency equals the premise one, we can infer entailment
    label = "entailment"

print(label)

