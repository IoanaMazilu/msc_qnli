# Premise: less than 400, what will be the difference between Mani and Rani's share?
# Hypothesis: 200, what will be the difference between Mani and Rani's share?
# Golden Label: neutral

share_difference_premise = 400
share_difference_hypothesis = 200

# the hypothesis refers to the same share difference mentioned in the premise
if share_difference_hypothesis >= share_difference_premise:
    # check if the value of 'share_difference_hypothesis' contradicts the estimate of less than 'share_difference_premise'
    label = "contradiction"
elif share_difference_hypothesis < share_difference_premise:
    # if the value of 'share_difference_hypothesis' is less than 'share_difference_premise', it can be entailed from the premise
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise one, but also cannot be explicitly entailed from it, we have a neutral relation
    label = "neutral"

print(label)

