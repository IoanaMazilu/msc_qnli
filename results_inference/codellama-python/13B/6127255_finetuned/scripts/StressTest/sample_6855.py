iron_coins_premise = 5
copper_coins_premise = 5
sum_range_premise_lower = 1
sum_range_premise_upper = 35

iron_coins_hypothesis = 5
copper_coins_hypothesis = 5
sum_range_hypothesis_lower = 5
sum_range_hypothesis_upper = 35

# the hypothesis refers to the same number of iron and copper coins and the same sum range as the premise
if iron_coins_hypothesis!= iron_coins_premise or copper_coins_hypothesis!= copper_coins_premise:
    # check if the number of coins in the hypothesis contradicts the number of coins in the premise
    label = "contradiction"
elif sum_range_hypothesis_lower < sum_range_premise_lower or sum_range_hypothesis_upper > sum_range_premise_upper:
    # check if the sum range in the hypothesis contradicts the sum range in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
