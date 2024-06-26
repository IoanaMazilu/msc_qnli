initial_customers_premise = 36.0
customers_left_premise = 19.0
remaining_customers_premise = 36.0 - customers_left_premise
customers_left_again_premise = 14.0

# the hypothesis refers to the number of customers, which are also mentioned in the premise
# compute the remaining number of customers in the premise
remaining_customers_premise = remaining_customers_premise - customers_left_again_premise
if remaining_customers_premise!= 3.0:
    # check if the number of remaining customers in the hypothesis contradicts the number of remaining customers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
