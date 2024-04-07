# Premise: How many oranges must Mary put back so that the average price of the pieces of fruit that she keeps is less than 78 ¢?
# Hypothesis: How many oranges must Mary put back so that the average price of the pieces of fruit that she keeps is 48 ¢?
# Golden Label: neutral

avg_price_premise = 78
avg_price_hypothesis = 48

# The hypothesis asks about the same situation as the premise but with a different average price
if avg_price_hypothesis >= avg_price_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the hypothesis value is less than the premise value, which does not contradict the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

