premise_total = 600
premise_share = 400
hypothesis_total = 400
hypothesis_share = 600

# the hypothesis refers to the total amount and the share of Greg
if hypothesis_total <= premise_total:
    # check if the estimate of 'hypothesis_total' contradicts the total amount in the premise
    label = "contradiction"
elif hypothesis_share!= premise_share:
    # check if the share of Greg in the hypothesis contradicts the share mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
