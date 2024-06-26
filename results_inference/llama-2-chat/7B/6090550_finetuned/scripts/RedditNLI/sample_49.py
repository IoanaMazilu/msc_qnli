# The premise and hypothesis mention the growth of global debt

# Convert the values to numerical quantities
premise_debt_growth = 57e12
hypothesis_debt_growth = 57e12

# Compare the growth rate of global debt in the premise and hypothesis
if premise_debt_growth!= hypothesis_debt_growth:
    # If the growth rates are different, it's a contradiction
    label = "contradiction"
else:
    # If the growth rates are the same, it's entailment
    label = "entailment"

print(label)
