premise_amount = 5120
hypothesis_amount = 1000

# the premise mentions the amount drained from the Turkish economy in July 2017
# the hypothesis mentions the amount drained from the Polish economy in July 2017
if premise_amount!= hypothesis_amount:
    # check if the amount drained in the hypothesis contradicts the amount drained in the premise
    label = "contradiction"
else:
    # if the amounts are the same, we can infer entailment
    label = "entailment"

print(label)
