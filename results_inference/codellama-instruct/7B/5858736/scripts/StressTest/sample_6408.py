# Define variables with representative names for the numerical entities in both inputs
offer_percentage_premise = 20
offer_percentage_hypothesis = 80
shirt_price_premise = 100
shirt_price_hypothesis = 100

# Extract all quantities as valid numbers (integers or floats)
offer_percentage_premise = float(offer_percentage_premise)
offer_percentage_hypothesis = float(offer_percentage_hypothesis)
shirt_price_premise = float(shirt_price_premise)
shirt_price_hypothesis = float(shirt_price_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if offer_percentage_hypothesis >= offer_percentage_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'offer_percentage_premise'
    label = "contradiction"
elif shirt_price_hypothesis!= shirt_price_premise:
    # Check if the number of shirts bought in the hypothesis contradicts the number of shirts bought reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
