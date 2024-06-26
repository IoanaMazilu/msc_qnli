price_premise = 5.1
price_hypothesis = 5.1

# the hypothesis and premise mention the price of the deal
if price_premise != price_hypothesis:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
