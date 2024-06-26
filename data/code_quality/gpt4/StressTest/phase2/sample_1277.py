iron_coins_premise = 5
copper_coins_premise = 15
sum_range_premise = (1, 160)

iron_coins_hypothesis = 5
copper_coins_hypothesis = 15
sum_range_hypothesis = (8, 160)

# the hypothesis refers to the same scenario as the premise, but with a different sum range
if iron_coins_hypothesis != iron_coins_premise or copper_coins_hypothesis != copper_coins_premise:
    # check if the number of iron or copper coins in the hypothesis contradicts the number of coins mentioned in the premise
    label = "contradiction"
elif sum_range_hypothesis[0] < sum_range_premise[0] or sum_range_hypothesis[1] != sum_range_premise[1]:
    # check if the sum range in the hypothesis contradicts the sum range in the premise
    # it's a contradiction if the lower bound of the sum range is less than the premise OR if the upper bound does not match
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
