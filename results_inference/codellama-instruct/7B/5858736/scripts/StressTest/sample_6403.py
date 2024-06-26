premise_machine_a = 0.8
premise_machine_b = 0.2
hypothesis_machine_a = 0.8
hypothesis_machine_b = 0.2

# the hypothesis values are consistent with the premise values
if hypothesis_machine_a == premise_machine_a and hypothesis_machine_b == premise_machine_b:
    label = "entailment"
# the hypothesis values contradict the premise values
elif hypothesis_machine_a!= premise_machine_a or hypothesis_machine_b!= premise_machine_b:
    label = "contradiction"
# the hypothesis values are consistent with the premise values but cannot be explicitly entailed from the premise
else:
    label = "neutral"

print(label)
