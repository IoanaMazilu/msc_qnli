# Define variables for the numerical entities in the premise
bought_earmuffs_premise_before_dec = 6444.0
bought_earmuffs_premise_during_dec = 1346.0

# Define variables for the numerical entities in the hypothesis
sold_earmuffs_hypothesis = 5100.0

# Extract all quantities as valid numbers
bought_earmuffs_premise_before_dec = float(bought_earmuffs_premise_before_dec)
bought_earmuffs_premise_during_dec = float(bought_earmuffs_premise_during_dec)
sold_earmuffs_hypothesis = float(sold_earmuffs_hypothesis)

# Calculate the total number of earmuffs bought during December
bought_earmuffs_during_dec = bought_earmuffs_premise_before_dec - bought_earmuffs_premise_during_dec

# Compare the total number of earmuffs bought during December with the number of earmuffs sold in December
if bought_earmuffs_during_dec == sold_earmuffs_hypothesis:
    # If the total number of earmuffs bought during December is equal to the number of earmuffs sold in December, we can infer entailment
    label = "entailment"
else:
    # If the total number of earmuffs bought during December is not equal to the number of earmuffs sold in December, we can infer contradiction
    label = "contradiction"

print(label)
