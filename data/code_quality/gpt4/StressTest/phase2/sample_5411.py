iron_coins_premise = 5
copper_coins_premise = 10
sum_premise_start = 1
sum_premise_end = 60

iron_coins_hypothesis = 5
copper_coins_hypothesis = 10
sum_hypothesis_start = 6
sum_hypothesis_end = 60

# the hypothesis refers to the same number of iron and copper coins as the premise
if iron_coins_hypothesis != iron_coins_premise or copper_coins_hypothesis != copper_coins_premise:
    # check if the hypothesis contradicts the premise in terms of the number of coins
    label = "contradiction"
elif sum_hypothesis_start < sum_premise_start or sum_hypothesis_end != sum_premise_end:
    # check if the hypothesis contradicts the premise in terms of the range of sums
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise in any way, it can be entailed from the premise
    label = "entailment"

print(label)
