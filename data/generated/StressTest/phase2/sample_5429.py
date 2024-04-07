# Premise: At a bank, the service charges for transactions were US Dollar 1 for every 5 transactions.
# Hypothesis: At a bank, the service charges for transactions were US Dollar more than 1 for every 5 transactions.
# Golden Label: contradiction

service_charge_premise = 1
service_charge_hypothesis = 1

# the hypothesis refers to service charges for transactions mentioned in the premise
if service_charge_hypothesis <= service_charge_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)

