price_premise = 2.5
price_hypothesis = 2.5

# the hypothesis and premise mention the same price
if price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same price
    # however, the premise does not mention any comparison between the price in the premise and the price in the hypothesis
    # therefore, we cannot infer entailment
    label = "neutral"

print(label)
