commute_diff_premise = 2
commute_diff_hypothesis = 6

# The hypothesis refers to the difference in time it takes Darcy to commute to work by walking and by riding the train, which is also mentioned in the premise
if commute_diff_hypothesis < commute_diff_premise:
    # If the hypothesis difference value is less than the premise value, it contradicts the premise
    label = "contradiction"
elif commute_diff_hypothesis == commute_diff_premise:
    # If the hypothesis difference value is equal to the premise value, it entails the premise
    label = "entailment"
else:
    # If the hypothesis difference value is more than the premise value, it does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
