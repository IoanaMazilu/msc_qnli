average_price_premise = 45
average_price_hypothesis = 75

# the hypothesis refers to an event similar to the one mentioned in the premise
if average_price_hypothesis < average_price_premise:
    # check if the average price in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif average_price_hypothesis > average_price_premise:
    # check if the average price in the hypothesis is greater than the one in the premise
    label = "neutral"
else:
    # if the average prices do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
