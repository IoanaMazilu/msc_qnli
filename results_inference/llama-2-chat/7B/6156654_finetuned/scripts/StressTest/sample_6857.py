coins_iron = 5
coins_copper = 5
total_coins = coins_iron + coins_copper

# the hypothesis talks about the total number of coins and the range of possible sums, which is also mentioned in the premise
if total_coins < 1:
    # the premise states that Matt has at least 1 coin, which contradicts the hypothesis
    label = "contradiction"
elif total_coins > 35:
    # the premise states that Matt has at most 35 coins, which contradicts the hypothesis
    label = "contradiction"
else:
    # the premise and hypothesis are neutral, as they both refer to the same number of coins and the same range of possible sums
    label = "neutral"

print(label)
