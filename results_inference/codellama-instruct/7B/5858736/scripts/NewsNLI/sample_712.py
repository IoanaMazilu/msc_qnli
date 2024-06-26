# Define variables for the numerical entities in the premise and hypothesis
premise_souvenirs_value = 100000
premise_souvenirs_origin = "China"
hypothesis_souvenirs_value = 100000
hypothesis_souvenirs_origin = "China"

# Extract all quantities as valid numbers
premise_souvenirs_value = float(premise_souvenirs_value)
hypothesis_souvenirs_value = float(hypothesis_souvenirs_value)

# Use brief comments to explain what comparison you do between the defined variables
if premise_souvenirs_value!= hypothesis_souvenirs_value:
    # Check if the value of the souvenirs in the hypothesis contradicts the value reported in the premise
    label = "contradiction"
elif premise_souvenirs_origin!= hypothesis_souvenirs_origin:
    # Check if the origin of the souvenirs in the hypothesis contradicts the origin reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
