# define variables for the numerical entities in the premise and hypothesis
bulk_carrier_length_premise = 180
bulk_carrier_length_hypothesis = 180
pirates_premise = 6
pirates_hypothesis = 6
attack_skiffs_premise = 2
attack_skiffs_hypothesis = 2

# check if the length of the bulk carrier in the hypothesis contradicts the length in the premise
if bulk_carrier_length_hypothesis!= bulk_carrier_length_premise:
    label = "contradiction"
# check if the number of pirates in the hypothesis contradicts the number of pirates in the premise
elif pirates_hypothesis!= pirates_premise:
    label = "contradiction"
# check if the number of attack skiffs in the hypothesis contradicts the number of attack skiffs in the premise
elif attack_skiffs_hypothesis!= attack_skiffs_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
