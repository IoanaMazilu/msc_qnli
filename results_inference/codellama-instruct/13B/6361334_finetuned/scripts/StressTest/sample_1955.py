loss_indu_premise = 2
loss_indu_hypothesis = 1

# the hypothesis refers to the number of years and the interest rate mentioned in the premise
if loss_indu_hypothesis <= loss_indu_premise:
    # check if the estimate of 'loss_indu_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'loss_indu_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
