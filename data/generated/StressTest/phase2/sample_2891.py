# Premise: How many oranges must Mary put back so that the average price of the pieces of fruit that she keeps is 44 ¢?
# Hypothesis: How many oranges must Mary put back so that the average price of the pieces of fruit that she keeps is less than 44 ¢?
# Golden Label: contradiction

average_price_premise = 44
average_price_hypothesis = 44

# the hypothesis refers to the average price of the pieces of fruit that Mary keeps, also mentioned in the premise
if average_price_hypothesis >= average_price_premise:
    # check if the hypothesis value contradicts the premise's average price
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

