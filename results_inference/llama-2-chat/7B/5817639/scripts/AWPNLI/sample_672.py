customers_premise = 36.0
customers_hypothesis = 3.0

# the hypothesis refers to the number of customers, which is also mentioned in the premise
# compute the total number of customers in the premise
total_customers_premise = customers_premise + customers_hypothesis

# check if the number of customers in the hypothesis contradicts the number of customers from the premise
if total_customers_hypothesis!= total_customers_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
