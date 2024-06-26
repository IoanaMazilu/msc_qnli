customers_premise = 36.0
left_customers_premise = 19.0
remaining_customers_premise = 16.0
left_remaining_customers_premise = 14.0

# the hypothesis refers to the number of customers, which are also mentioned in the premise
# compute the total number of customers in the premise
total_customers_premise = customers_premise + left_customers_premise + remaining_customers_premise + left_remaining_customers_premise
if total_customers_premise!= 3.0:
    # check if the number of customers in the hypothesis contradicts the number of customers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)