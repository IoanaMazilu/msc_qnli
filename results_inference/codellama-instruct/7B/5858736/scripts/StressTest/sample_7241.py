# Define variables with representative names for the numerical entities in both inputs
father_age = 60
ayisha_age = 10

# Extract all quantities as valid numbers (integers or floats)
father_age_num = 60
ayisha_age_num = 10

# Use brief comments to explain what comparison you do between the defined variables
if ayisha_age_num < father_age_num / 6:
    # Check if Ayisha's age is less than 1/6 th of her father's age
    label = "contradiction"
else:
    # If Ayisha's age is not less than 1/6 th of her father's age, we can infer entailment
    label = "entailment"

print(label)
