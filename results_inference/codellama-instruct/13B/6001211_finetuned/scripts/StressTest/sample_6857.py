lower_limit_premise = 1
upper_limit_premise = 35
lower_limit_hypothesis = 1
upper_limit_hypothesis = 35

# the hypothesis refers to the range of sums that Matt can make with his coins, which is also mentioned in the premise
if lower_limit_hypothesis <= lower_limit_premise:
    # check if the lower limit of the range in the hypothesis contradicts the lower limit of the range in the premise
    label = "contradiction"
elif upper_limit_hypothesis!= upper_limit_premise:
    # check if the upper limit of the range in the hypothesis contradicts the upper limit of the range in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
