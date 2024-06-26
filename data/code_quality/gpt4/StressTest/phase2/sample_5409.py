iron_coins_premise = 5
copper_coins_premise = 10
sum_range_premise_min = 1
sum_range_premise_max = 60

iron_coins_hypothesis = 5
copper_coins_hypothesis = 10
sum_range_hypothesis_min = 3
sum_range_hypothesis_max = 60

# the hypothesis refers to the same number of iron and copper coins, and the same sum range as in the premise
if iron_coins_premise != iron_coins_hypothesis or copper_coins_premise != copper_coins_hypothesis:
    # check if the number of coins mentioned in the hypothesis contradicts the premise
    label = "contradiction"
elif sum_range_premise_min > sum_range_hypothesis_min or sum_range_premise_max != sum_range_hypothesis_max:
    # check if the sum range in the hypothesis contradicts the sum range in the premise
    label = "contradiction"
else:
    # if the number of coins and sum range in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
