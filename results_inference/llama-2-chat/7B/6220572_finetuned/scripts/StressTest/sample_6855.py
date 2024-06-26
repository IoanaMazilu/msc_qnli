iron_coins_premise = 5
copper_coins_premise = 5

# the hypothesis talks about the number of different sums Matt can make with his coins, referenced also in the premise
if iron_coins_hypothesis >= iron_coins_premise or copper_coins_hypothesis >= copper_coins_premise:
    # check if the hypothesis values contradict the number of iron or copper coins reported in the premise
    label = "contradiction"
else:
    # any number of different sums less than 'iron_coins_premise' or 'copper_coins_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
