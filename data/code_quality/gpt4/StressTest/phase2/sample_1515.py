john_profit_premise = 800
john_profit_hypothesis = 400

# the hypothesis talks about the profit John made in comparison to Mike, as mentioned in the premise
if john_profit_hypothesis >= john_profit_premise:
    # check if the profit made by John in the hypothesis contradicts the profit made by John in the premise
    label = "contradiction"
else:
    # the hypothesis suggests a profit that is consistent with the premise but can't be explicitly entailed from it
    label = "neutral"

print(label)