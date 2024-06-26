loss_indu_premise = 2
loss_indu_hypothesis = 6
interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis refers to the number of years and interest rate mentioned in the premise
if loss_indu_hypothesis <= loss_indu_premise:
    # check if the estimate of 'loss_indu_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
