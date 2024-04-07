# Premise: 450 and she sold that to George for Rs.
# Hypothesis: 750 and she sold that to George for Rs.
# Golden Label: contradiction

price_premise = 450
price_hypothesis = 750

# the hypothesis talks about a price, referenced also in the premise
if price_hypothesis == price_premise:
    # check if the price in the hypothesis matches the price in the premise
    label = "entailment"
elif price_hypothesis < price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # the price in the premise is different from the price in the hypothesis
    # it doesn't contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

