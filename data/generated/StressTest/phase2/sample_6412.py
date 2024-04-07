# Premise: If there are more than 45 possible combinations in which Michael is not selected, what is the value of w?
# Hypothesis: If there are 55 possible combinations in which Michael is not selected, what is the value of w?
# Golden Label: neutral

combinations_premise = 45
combinations_hypothesis = 55

# the hypothesis talks about the number of combinations in which Michael is not selected, which is also mentioned in the premise
if combinations_hypothesis <= combinations_premise:
    # check if the number of combinations in the hypothesis contradicts the estimate of more than 'combinations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of combinations
    # any number of combinations greater than 'combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

