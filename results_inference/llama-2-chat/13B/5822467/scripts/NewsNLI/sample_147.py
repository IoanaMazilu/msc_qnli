eu_force_premise = 6
attack_skiffs_premise = 2
bulk_carrier_premise = 180

# define variables for the hypothesis
eu_force_hypothesis = 6
attack_skiffs_hypothesis = 2
bulk_carrier_hypothesis = 180

# compare the values of the variables
if eu_force_hypothesis == eu_force_premise and attack_skiffs_hypothesis == attack_skiffs_premise and bulk_carrier_hypothesis == bulk_carrier_premise:
    # if all the values are the same, we can infer entailment
    label = "entailment"
elif eu_force_hypothesis!= eu_force_premise or attack_skiffs_hypothesis!= attack_skiffs_premise or bulk_carrier_hypothesis!= bulk_carrier_premise:
    # if any of the values are different, we can infer contradiction
    label = "contradiction"
else:
    # if the values are different but we cannot infer entailment or contradiction, we can infer neutrality
    label = "neutral"

print(label)
