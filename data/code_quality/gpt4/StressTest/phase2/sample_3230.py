store_z_price_premise = 70
store_z_price_hypothesis = 70

# The hypothesis talks about the price of an item in store Z, referenced also in the premise
if store_z_price_hypothesis > store_z_price_premise:
    # Check if the hypothesis value contradicts the exact price 'store_z_price_premise' in the premise
    label = "entailment"
else:
    # If the hypothesis value is not more than the price in the premise, we have a contradiction
    label = "contradiction"

print(label)
