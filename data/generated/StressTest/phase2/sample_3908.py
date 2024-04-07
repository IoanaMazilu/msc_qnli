# Premise: How many oranges must Mary put back so that the average price of the pieces of fruit that she keeps is 50 ¢?
# Hypothesis: How many oranges must Mary put back so that the average price of the pieces of fruit that she keeps is 70 ¢?
# Golden Label: contradiction

avg_price_premise = 50
avg_price_hypothesis = 70

# the hypothesis refers to the average price of fruit that Mary keeps, also mentioned in the premise
if avg_price_premise != avg_price_hypothesis:
    # check if the average price in the hypothesis contradicts the average price mentioned in the premise
    label = "contradiction"
else:
    # if the average prices in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)
