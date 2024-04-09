customers_premise = 19.0
customers_left_premise = 14.0
new_customers_premise = 36.0

# define variables for the hypothesis
customers_hypothesis = 37.0

# compute the total number of customers in the premise
total_customers_premise = customers_premise + customers_left_premise + new_customers_premise

# compare the total number of customers in the hypothesis to the total number of customers in the premise
if customers_hypothesis!= total_customers_premise:
    # if the number of customers in the hypothesis contradicts the total number of customers in the premise,
    # then the hypothesis is in contradiction to the premise
    label = "contradiction"
else:
    # if the number of customers in the hypothesis is equal to the total number of customers in the premise,
    # then we can infer entailment
    label = "entailment"

print(label)
