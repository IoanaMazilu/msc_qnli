total_customers_premise = 7422.0
us_customers_premise = 723.0
total_customers_hypothesis = 8144.0

# the hypothesis refers to the total number of customers, which is also mentioned in the premise
# compute the total number of customers in the premise
total_customers_premise += us_customers_premise
if total_customers_hypothesis != total_customers_premise:
    # check if the number of customers in the hypothesis contradicts the number of customers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
