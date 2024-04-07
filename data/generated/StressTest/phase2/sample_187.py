# Premise: The ratio between the school ages of Neelam and Shaan is more than 3:6 respectively.
# Hypothesis: The ratio between the school ages of Neelam and Shaan is 5:6 respectively.
# Golden Label: neutral

ratio_premise = 3/6
ratio_hypothesis = 5/6

# the hypothesis refers to the ratio between the school ages of Neelam and Shaan mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the 'ratio_hypothesis' contradicts the estimate of more than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

