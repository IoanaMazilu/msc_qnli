total_amount_premise = 500
total_amount_hypothesis = 600

# the hypothesis refers to the total amount and the share of Greg, both mentioned in the premise
if total_amount_hypothesis <= total_amount_premise:
    # check if the estimate of 'total_amount_hypothesis' contradicts the number of total amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
