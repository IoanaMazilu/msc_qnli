iron_coins_premise = 5
copper_coins_premise = 5
sums_premise = 35

iron_coins_hypothesis = 5
copper_coins_hypothesis = 5
sums_hypothesis = 5

# the hypothesis refers to the number of different sums that can be made with a combination of coins
# the premise mentions the number of different sums that can be made with a combination of coins
# the hypothesis value is less than the premise value, so it contradicts the premise
if sums_hypothesis <= sums_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
