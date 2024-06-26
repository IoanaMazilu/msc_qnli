corporate_customers_premise = 70
corporate_customers_hypothesis = 40
banking_related_premise = 20
banking_related_hypothesis = 20
hq_usa_premise = 60
hq_usa_hypothesis = 60

# the hypothesis refers to the percentage of corporate customers, the percentage of them related to the banking sector, 
# and the percentage of them having their headquarters in the USA, mentioned in the premise
if corporate_customers_premise < corporate_customers_hypothesis:
    # check if the estimate of 'corporate_customers_hypothesis' contradicts the percentage of corporate customers in the premise
    label = "contradiction"
elif banking_related_hypothesis != banking_related_premise:
    # check if the percentage of banking-related customers in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
elif hq_usa_hypothesis != hq_usa_premise:
    # check if the percentage of USA-based customers in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentages do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
