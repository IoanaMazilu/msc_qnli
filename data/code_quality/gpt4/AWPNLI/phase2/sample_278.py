initial_customers_premise = 19.0
customers_left_premise = 14.0
additional_customers_premise = 36.0
total_customers_hypothesis = 41.0

# The hypothesis refers to the total number of customers, which are also mentioned in the premise
# Compute the total number of customers in the premise
total_customers_premise = initial_customers_premise - customers_left_premise + additional_customers_premise
if total_customers_hypothesis != total_customers_premise:
    # Check if the number of customers in the hypothesis contradicts the number of customers from the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
