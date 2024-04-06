# Premise: A cell phone company has a total of 7422.0 customers across the world, and they get 723.0 more customers in the United States.
# Hypothesis: They will have 8145.0 total customers.
# Golden Label: entailment

total_customers_premise = 7422.0
new_us_customers_premise = 723.0
total_customers_hypothesis = 8145.0

# the hypothesis refers to the total number of customers, which is also mentioned in the premise
# compute the new total number of customers in the premise
new_total_customers_premise = total_customers_premise + new_us_customers_premise
if new_total_customers_premise != total_customers_hypothesis:
    # check if the new total number of customers in the hypothesis contradicts the new total number of customers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

