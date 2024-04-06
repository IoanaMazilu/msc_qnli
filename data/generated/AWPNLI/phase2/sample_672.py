# Premise: A waiter had 36.0 customers to wait on, and 19.0 of the customers left and then 14.0 of the remaining customers left.
# Hypothesis: He would have 3.0 customers.
# Golden Label: entailment

total_customers_premise = 36.0
first_left_customers_premise = 19.0
second_left_customers_premise = 14.0
remaining_customers_hypothesis = 3.0

# the hypothesis refers to the number of remaining customers, which is also mentioned in the premise
# calculate the number of remaining customers from the premise
remaining_customers_premise = total_customers_premise - first_left_customers_premise - second_left_customers_premise

if remaining_customers_hypothesis != remaining_customers_premise:
    # check if the number of remaining customers in the hypothesis contradicts the number of remaining customers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
