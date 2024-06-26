premise_machine_a = 0.8
premise_machine_b = 0.2
hypothesis_machine_a = 0.8
hypothesis_machine_b = 0.2

# the hypothesis refers to the percentage of components that would be manufactured by each machine
if hypothesis_machine_a!= premise_machine_a or hypothesis_machine_b!= premise_machine_b:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif hypothesis_machine_a + hypothesis_machine_b!= 1:
    # check if the sum of the hypothesis values is not equal to 1
    label = "contradiction"
else:
    # if the hypothesis values and the premise ones are consistent, we can infer entailment
    label = "entailment"

print(label)
