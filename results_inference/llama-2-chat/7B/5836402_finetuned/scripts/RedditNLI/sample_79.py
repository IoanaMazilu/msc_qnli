price_premise = 5.1
price_hypothesis = 5.1

# the hypothesis and premise mention the price of the deal for Costa Coffee
if price_hypothesis!= price_premise:
    # check if the price of the deal in the hypothesis contradicts the price of the deal in the premise
    label = "contradiction"
else:
    # if the price of the deal in the hypothesis does not contradict the price of the deal in the premise, we can infer entailment
    label = "entailment"

print(label)
