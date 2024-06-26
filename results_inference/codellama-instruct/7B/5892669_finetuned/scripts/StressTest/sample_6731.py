average_price_premise = 50
average_price_hypothesis = 40

# the hypothesis refers to the average price of the fruit mentioned in the premise
if average_price_hypothesis!= average_price_premise:
    # check if the average price in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
