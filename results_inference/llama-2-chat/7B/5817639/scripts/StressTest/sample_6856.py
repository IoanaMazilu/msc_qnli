five_iron_coins_premise = 5
five_copper_coins_premise = 5

# the hypothesis talks about the number of different sums Matt can make with a combination of his coins
if five_iron_coins_hypothesis <= five_iron_coins_premise:
    # check if the hypothesis value contradicts the estimate of 'five_iron_coins_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of coins, but the hypothesis provides a more specific value
    label = "entailment"

print(label)
