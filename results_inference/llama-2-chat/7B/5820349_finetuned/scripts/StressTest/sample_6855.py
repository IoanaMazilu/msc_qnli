iron_coins_premise = 5
iron_coins_hypothesis = 5
copper_coins_premise = 5
copper_coins_hypothesis = 5
sum_range_premise = 1
sum_range_hypothesis = 5

# the hypothesis talks about the number of iron and copper coins Matt has, and the range of sums he can make
if iron_coins_hypothesis!= iron_coins_premise or copper_coins_hypothesis!= copper_coins_premise:
    # check if the number of coins in the hypothesis contradicts the number of coins in the premise
    label = "contradiction"
elif sum_range_hypothesis >= sum_range_premise:
    # check if the range of sums in the hypothesis contradicts the range of sums in the premise
    label = "contradiction"
else:
    # the premise and hypothesis both talk about the same scenario, but the hypothesis introduces a new range of sums
    # this new range of sums cannot be explicitly entailed from the premise, so the relation is neutral
    label = "neutral"

print(label)
