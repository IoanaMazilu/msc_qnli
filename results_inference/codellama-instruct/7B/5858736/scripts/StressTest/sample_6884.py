# Define variables for the numerical entities in both inputs
bonds_sold_premise = 50
bonds_sold_hypothesis = 70

# Extract all quantities as valid numbers
bonds_sold_premise = int(bonds_sold_premise)
bonds_sold_hypothesis = int(bonds_sold_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if bonds_sold_hypothesis <= bonds_sold_premise:
    # Check if the hypothesis value contradicts the estimate of $50 or $100 denominations only
    label = "contradiction"
else:
    # The hypothesis value is greater than $50 or $100 denominations only, which means that Robert purchased more than 50 or 100 US saving bonds
    label = "entailment"

print(label)
