# Define variables for premise and hypothesis
premise_variables = {"Manchester City": 0, "Leicester": 0, "FA Cup": 0}
hypothesis_variables = {"Manchester City": 0, "Leicester": 1, "replay": 0}

# Extract quantities from premise and hypothesis
premise_quantities = {k: v for k, v in premise_variables.items() if v is not None}
hypothesis_quantities = {k: v for k, v in hypothesis_variables.items() if v is not None}

# Check for contradictions
contradiction_check = False
for k, v in hypothesis_quantities.items():
    if v!= hypothesis_variables[k]:
        contradiction_check = True
        break
if contradiction_check:
    label = "contradiction"
else:
    # Check for entailment
    entailment_check = False
    for k, v in premise_quantities.items():
        if v!= premise_variables[k]:
            entailment_check = True
            break
    if entailment_check:
        label = "entailment"
    else:
        label = "neutral"

print(label)
