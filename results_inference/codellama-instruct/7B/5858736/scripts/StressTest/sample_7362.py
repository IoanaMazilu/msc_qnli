# Define variables with representative names for the numerical entities in both inputs
discount_premise = 30
listed_price_premise = 100
discount_hypothesis = 10

# Extract all quantities as valid numbers
discount_premise = float(discount_premise)
listed_price_premise = float(listed_price_premise)
discount_hypothesis = float(discount_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if discount_hypothesis <= discount_premise:
    # Check if the estimate of 'discount_hypothesis' contradicts the discount mentioned in the premise
    label = "contradiction"
elif listed_price_premise * (1 - discount_premise/100) <= listed_price_premise * (1 - discount_hypothesis/100):
    # Check if the discount in the hypothesis contradicts the discount mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
