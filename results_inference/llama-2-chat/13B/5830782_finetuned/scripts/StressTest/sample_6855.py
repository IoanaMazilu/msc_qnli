iron_coins_premise = 5
copper_coins_premise = 5
sum_premise_min = 1
sum_premise_max = 35

iron_coins_hypothesis = 5
copper_coins_hypothesis = 5
sum_hypothesis_min = 5
sum_hypothesis_max = 35

# the hypothesis refers to the number of iron and copper coins Matt has, and the range of sums he can make
if iron_coins_premise!= iron_coins_hypothesis:
    # check if the number of iron coins in the hypothesis contradicts the number of iron coins in the premise
    label = "contradiction"
elif copper_coins_premise!= copper_coins_hypothesis:
    # check if the number of copper coins in the hypothesis contradicts the number of copper coins in the premise
    label = "contradiction"
elif sum_hypothesis_min < sum_premise_min:
    # check if the minimum sum in the hypothesis contradicts the minimum sum in the premise
    label = "contradiction"
elif sum_hypothesis_max!= sum_premise_max:
    # check if the maximum sum in the hypothesis contradicts the maximum sum in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
