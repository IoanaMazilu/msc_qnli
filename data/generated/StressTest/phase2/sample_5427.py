# Premise: At a bank, the service charges for transactions were US Dollar 1 for every 5 transactions.
# Hypothesis: At a bank, the service charges for transactions were US Dollar less than 3 for every 5 transactions.
# Golden Label: entailment

service_charge_premise = 1
service_charge_hypothesis = 3

# the hypothesis refers to the service charges for transactions mentioned in the premise
if service_charge_hypothesis >= service_charge_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

