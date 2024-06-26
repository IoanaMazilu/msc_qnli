customers_left_premise = 14.0
customers_new_premise = 36.0
total_customers_hypothesis = 37.0

# the hypothesis refers to the total number of customers the waiter would have, which is also mentioned in the premise
if customers_left_premise + customers_new_premise!= total_customers_hypothesis:
    # check if the total number of customers in the hypothesis contradicts the total number of customers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
