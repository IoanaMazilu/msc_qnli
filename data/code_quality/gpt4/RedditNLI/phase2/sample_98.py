shrink_percentage_premise = 1.0
fall_amount_hypothesis = 6

# the premise and hypothesis mention the decrease in net foreign assets of the Saudi central bank
# however, the premise gives the decrease in terms of a percentage, while the hypothesis gives it as an amount in billions of dollars
# since we don't know the initial amount of the assets, we cannot convert between the two units
label = "neutral"

print(label)
