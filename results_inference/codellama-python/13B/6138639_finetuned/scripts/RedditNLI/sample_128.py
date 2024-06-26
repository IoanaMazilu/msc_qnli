price_premise = 7.2
price_hypothesis = 7.15

# the hypothesis and premise mention the price of the coffee tie-up
if price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
