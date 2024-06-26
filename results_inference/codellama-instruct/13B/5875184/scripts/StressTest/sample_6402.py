premise_components = 60
premise_percent_machine_a = 80
premise_percent_machine_b = 20

hypothesis_components = 30
hypothesis_percent_machine_a = 80
hypothesis_percent_machine_b = 20

# check if the hypothesis value contradicts the premise value
if hypothesis_components < premise_components:
    label = "contradiction"
elif hypothesis_percent_machine_a!= premise_percent_machine_a or hypothesis_percent_machine_b!= premise_percent_machine_b:
    label = "contradiction"
else:
    label = "entailment"

print(label)
