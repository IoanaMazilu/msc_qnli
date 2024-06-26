remaining_customers_premise = 36.0 - 19.0 - 14.0
remaining_customers_hypothesis = 3.0

# the hypothesis refers to the number of remaining customers, which is also mentioned in the premise
if remaining_customers_hypothesis!= remaining_customers_premise:
    # check if the number of remaining customers in the hypothesis contradicts the number of remaining customers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
