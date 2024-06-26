coin1_premise = 2
coin2_premise = 5
coin1_hypothesis = 6
coin2_hypothesis = 5

# the hypothesis refers to the amount of coins mentioned in the premise
if coin1_hypothesis != coin1_premise or coin2_hypothesis != coin2_premise:
    # check if the amount of coins in the hypothesis contradicts the amount of coins reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
