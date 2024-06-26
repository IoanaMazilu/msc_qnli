customers_waited_premise = 19.0
customers_left_premise = 14.0
customers_arrived_hypothesis = 36.0

# the hypothesis refers to the number of customers, which are also mentioned in the premise
# compute the total number of customers in the premise
total_customers_premise = customers_waited_premise + customers_left_premise
if total_customers_hypothesis!= total_customers_premise:
    # check if the number of customers in the hypothesis contradicts the number of customers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)