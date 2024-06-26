# Define variables for the numerical entities in the premise and hypothesis
premise_hotels_under_200 = 200
hypothesis_hotels_under_200 = 200

# Extract all quantities as valid numbers
premise_hotels_under_200 = float(premise_hotels_under_200)
hypothesis_hotels_under_200 = float(hypothesis_hotels_under_200)

# Use brief comments to explain what comparison you do between the defined variables
if premise_hotels_under_200!= hypothesis_hotels_under_200:
    # Check if the number of hotels under $200 in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
