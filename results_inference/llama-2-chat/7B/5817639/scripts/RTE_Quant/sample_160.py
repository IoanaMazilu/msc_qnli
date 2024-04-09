# Define variables for premise and hypothesis
premise_centrifuges = 54000
premise_megawatt = 1000

# Extract quantities from the hypothesis
hypothesis_centrifuges = 54000
hypothesis_megawatt = 1000

# Check for contradictions
if hypothesis_centrifuges!= premise_centrifuges:
    label = "contradiction"
elif hypothesis_megawatt!= premise_megawatt:
    label = "contradiction"
else:
    # If no contradictions found, check for entailment
    label = "entailment"

print(label)
