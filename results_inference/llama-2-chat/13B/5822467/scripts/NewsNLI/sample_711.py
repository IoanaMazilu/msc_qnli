# define variables with representative names for the numerical entities in both inputs
grants_premise = 45000
grants_hypothesis = 45000

# extract all quantities as valid numbers (integers or floats)
grants_premise_value = float(grants_premise)
grants_hypothesis_value = float(grants_hypothesis)

# compare the values of the grants mentioned in the premise and hypothesis
if grants_hypothesis_value!= grants_premise_value:
    # if the values are not the same, we can infer contradiction
    label = "contradiction"
else:
    # if the values are the same, we can infer neutrality
    label = "neutral"

print(label)
