service_charge_premise = 3
service_charge_hypothesis = 1

# the hypothesis talks about the service charges for transactions at a bank, also referenced in the premise
if service_charge_hypothesis >= service_charge_premise:
    # check if the hypothesis value contradicts the estimate of less than 'service_charge_premise'
    label = "contradiction"
elif service_charge_hypothesis < service_charge_premise:
    # if the service charges in the hypothesis are less than those in the premise, we can infer entailment
    label = "entailment"

print(label)