# Premise: How many oranges must Mary put back so that the average price of the pieces of fruit that she keeps is 45 ¢?
# Hypothesis: How many oranges must Mary put back so that the average price of the pieces of fruit that she keeps is less than 45 ¢?
# Golden Label: contradiction

average_price_premise = 45
average_price_hypothesis = 45

# the hypothesis asks about the number of oranges Mary must put back to make the average price of fruit she keeps less than in the premise
if average_price_hypothesis >= average_price_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise and hypothesis are both questions about the same situation, but with different desired outcomes
    # thus, one does not entail or contradict the other
    label = "neutral"

print(label)

