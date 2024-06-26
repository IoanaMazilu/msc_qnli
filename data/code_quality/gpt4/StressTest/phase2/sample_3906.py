average_price_premise = 50
average_price_hypothesis = 40

# the hypothesis and premise both refer to the average price of remaining fruit
if average_price_premise < average_price_hypothesis:
    # check if the premise value contradicts the hypothesis's estimate of 'more than average_price_hypothesis'
    label = "contradiction"
elif average_price_premise > average_price_hypothesis:
    # check if the premise value is greater than the hypothesis's estimate
    label = "entailment"
else:
    # if the premise and hypothesis values don't contradict each other, we can infer neutrality
    label = "neutral"

print(label)
