premise_quantity = 20
premise_rate = 275
hypothesis_quantity = 20
hypothesis_rate = 375

# the hypothesis refers to the number of dozens and the rate of purchase
if premise_quantity <= hypothesis_quantity:
    # check if the estimate of 'hypothesis_quantity' contradicts the number of dozens in the premise
    label = "contradiction"
elif premise_rate <= hypothesis_rate:
    # check if the estimate of 'hypothesis_rate' contradicts the rate of purchase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
