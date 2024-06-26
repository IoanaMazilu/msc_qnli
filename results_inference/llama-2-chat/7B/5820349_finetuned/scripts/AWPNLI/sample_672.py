initial_customers_premise = 36.0
first_group_customers_premise = 19.0
second_group_customers_premise = 14.0
remaining_customers_hypothesis = 3.0

# the hypothesis refers to the number of remaining customers, which can be computed from the premise
# compute the number of remaining customers in the premise
remaining_customers_premise = initial_customers_premise - first_group_customers_premise - second_group_customers_premise
if remaining_customers_hypothesis!= remaining_customers_premise:
    # check if the number of remaining customers in the hypothesis contradicts the number of remaining customers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
