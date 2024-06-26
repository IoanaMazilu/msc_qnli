price_premise = 7500
price_hypothesis = 7400

# the hypothesis and premise mention the price of nifty
if price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the price in the hypothesis does not contradict the price in the premise, we can infer entailment
    label = "entailment"

print(label)
