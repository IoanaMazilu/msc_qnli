lower_sum_limit_premise = 7
lower_sum_limit_hypothesis = 1
upper_sum_limit_premise = 70
upper_sum_limit_hypothesis = 70

# the hypothesis refers to the same situation as the premise, but changes the lower limit of the sums that can be made with the coins
if lower_sum_limit_hypothesis < lower_sum_limit_premise:
    # check if the new lower limit in the hypothesis contradicts the premise
    label = "contradiction"
elif upper_sum_limit_hypothesis != upper_sum_limit_premise:
    # check if the upper limit of the sums in the hypothesis contradicts the one from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
