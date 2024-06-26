customers_premise = 19.0
customers_left_premise = 14.0
customers_added_premise = 36.0
total_customers_hypothesis = 37.0

# the hypothesis refers to the total number of customers, which are also mentioned in the premise
# compute the total number of customers in the premise
total_customers_premise = customers_premise + customers_left_premise + customers_added_premise
if total_customers_hypothesis!= total_customers_premise:
    # check if the number of customers in the hypothesis contradicts the number of customers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)