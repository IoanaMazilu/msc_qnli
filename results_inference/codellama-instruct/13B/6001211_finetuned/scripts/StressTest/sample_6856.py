lower_limit_premise = 5
upper_limit_premise = 35
lower_limit_hypothesis = 1
upper_limit_hypothesis = 35

# the hypothesis refers to the range of sums that Matt can make with his coins, also mentioned in the premise
if lower_limit_hypothesis < lower_limit_premise or upper_limit_hypothesis > upper_limit_premise:
    # check if the range of sums in the hypothesis contradicts the range of sums mentioned in the premise
    label = "contradiction"
else:
    # if the range of sums in the hypothesis does not contradict the range of sums in the premise, we can infer entailment
    label = "entailment"

print(label)
