premise_loss = 
hypothesis_loss = 

# the hypothesis refers to the number of years and interest rate mentioned in the premise
if hypothesis_loss <= premise_loss:
    # check if the estimate of 'hypothesis_loss' contradicts the number of years and interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
