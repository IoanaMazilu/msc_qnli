# Premise: How many oranges must Mary put back so that the average price of the pieces of fruit that she keeps is less than 54 ¢?
# Hypothesis: How many oranges must Mary put back so that the average price of the pieces of fruit that she keeps is 44 ¢?
# Golden Label: neutral

average_price_premise = 54
average_price_hypothesis = 44

# the hypothesis talks about the average price of the pieces of fruit Mary keeps, referenced also in the premise
if average_price_hypothesis >= average_price_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average price
    # any average price less than 'average_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

