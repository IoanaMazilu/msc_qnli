iron_coins_premise = 5
copper_coins_premise = 5

# the hypothesis talks about the number of coins in a combination, referenced also in the premise
if iron_coins_premise + copper_coins_premise <= 35:
    # check if the hypothesis value contradicts the estimate of less than '35'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of coins
    # any number of coins greater than '35' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
