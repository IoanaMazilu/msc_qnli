coins_iron_premise = 5
coins_iron_hypothesis = 5
coins_copper_premise = 5
coins_copper_hypothesis = 5
sums_premise = 1
sums_hypothesis = 35

# the hypothesis refers to the number of coins and the sums that can be made
if coins_iron_hypothesis!= coins_iron_premise or coins_copper_hypothesis!= coins_copper_premise:
    # check if the number of coins in the hypothesis contradicts the number of coins in the premise
    label = "contradiction"
elif sums_hypothesis < sums_premise:
    # check if the sum in the hypothesis contradicts the sum in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones
    label = "neutral"

print(label)
