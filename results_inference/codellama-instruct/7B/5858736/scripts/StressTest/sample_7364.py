# Define variables for the numerical entities in the premise and hypothesis
discount_premise = 30
listed_price_premise = 100
calculator_price_premise = 70

# Define variables for the numerical entities in the hypothesis
discount_hypothesis = 30
listed_price_hypothesis = 100
calculator_price_hypothesis = 70

# Calculate the discounted price for the premise
discounted_price_premise = listed_price_premise - (listed_price_premise * discount_premise / 100)

# Calculate the discounted price for the hypothesis
discounted_price_hypothesis = listed_price_hypothesis - (listed_price_hypothesis * discount_hypothesis / 100)

# Check if the discounted price in the hypothesis is less than the discounted price in the premise
if discounted_price_hypothesis <= discounted_price_premise:
    # The hypothesis is entailed from the premise
    label = "entailment"
else:
    # The hypothesis is not entailed from the premise
    label = "contradiction"

print(label)
