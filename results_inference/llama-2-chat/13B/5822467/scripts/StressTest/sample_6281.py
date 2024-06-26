ratio_premise = 7:3:2
ratio_hypothesis = 5:3:2

# compare the ratio of questions submitted by each person in the premise and hypothesis
if ratio_premise == ratio_hypothesis:
    # the hypothesis is consistent with the premise, so neutral
    label = "neutral"
elif ratio_premise > ratio_hypothesis:
    # the premise indicates a higher ratio of questions submitted by Rajat and Vikas, which contradicts the hypothesis
    label = "contradiction"
else:
    # the hypothesis indicates a lower ratio of questions submitted by Rajat and Vikas, which entails the premise
    label = "entailment"

print(label)
