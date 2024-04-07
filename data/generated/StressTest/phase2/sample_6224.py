# Premise: 200, what will be the difference between Mani and Rani's share?
# Hypothesis: more than 200, what will be the difference between Mani and Rani's share?
# Golden Label: contradiction

share_difference_premise = 200
share_difference_hypothesis = 200

# the hypothesis refers to the difference between Mani and Rani's share mentioned in the premise
if share_difference_hypothesis > share_difference_premise:
    # check if the hypothesis estimate contradicts the exact difference in the premise
    label = "contradiction"
elif share_difference_hypothesis == share_difference_premise:
    # the premise gives an exact value for the share difference
    # the same value in the hypothesis can be explicitly entailed from the premise
    label = "entailment"
else:
    # any value less than 'share_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

