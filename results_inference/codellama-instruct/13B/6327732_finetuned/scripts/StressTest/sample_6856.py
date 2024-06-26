premise_iron_coins = 5
premise_copper_coins = 5
hypothesis_iron_coins = 5
hypothesis_copper_coins = 5

# the hypothesis refers to the number of coins and their types mentioned in the premise
if premise_iron_coins!= hypothesis_iron_coins or premise_copper_coins!= hypothesis_copper_coins:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of coins and their types
    # any combination of coins with the same number of iron and copper coins is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
