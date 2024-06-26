# Define variables with representative names for the numerical entities in both inputs
num_boys = 6
num_girls = 4
num_committee_members = 4

# Extract all quantities as valid numbers (integers or floats)
num_boys = int(num_boys)
num_girls = int(num_girls)
num_committee_members = int(num_committee_members)

# Use brief comments to explain what comparison you do between the defined variables
if num_boys + num_girls < num_committee_members:
    # Check if the number of boys and girls combined is less than the number of committee members
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
