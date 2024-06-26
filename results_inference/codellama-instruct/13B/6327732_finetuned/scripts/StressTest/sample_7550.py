premise_saving_amount = 100
hypothesis_saving_amount = 80

# the hypothesis refers to the saving amount mentioned in the premise
if hypothesis_saving_amount <= premise_saving_amount:
    # check if the estimate of 'hypothesis_saving_amount' contradicts the saving amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
