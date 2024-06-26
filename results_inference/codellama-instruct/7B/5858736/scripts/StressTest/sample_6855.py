iron_coins_premise = 5
copper_coins_premise = 5

# the hypothesis talks about the number of iron and copper coins mentioned in the premise
if iron_coins_premise <= copper_coins_premise:
    # check if the estimate of 'copper_coins_hypothesis' contradicts the number of copper coins in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of copper coins
    # any number of copper coins greater than 'copper_coins_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
