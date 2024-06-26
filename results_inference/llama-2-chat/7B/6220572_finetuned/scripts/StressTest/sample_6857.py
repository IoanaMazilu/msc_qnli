iron_coins_premise = 5
copper_coins_premise = 5

# the hypothesis refers to the number of iron and copper coins mentioned in the premise
if iron_coins_hypothesis!= iron_coins_premise or copper_coins_hypothesis!= copper_coins_premise:
    # check if the number of iron or copper coins in the hypothesis contradicts the number of coins in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of coins
    # any number of coins consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
