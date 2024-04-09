# Variables to represent the entities in the input sentences
premise_factors = []
hypothesis_factors = []

# Extract the factors from the input sentences
premise_text = "U.S. economy a world beater because of 5 factors."
hypothesis_text = "What's making US economy a world beater? 5 factors."

premise_factors = re.findall(r'\w+', premise_text)
hypothesis_factors = re.findall(r'\w+', hypothesis_text)

# Define variables to represent the quantities in the input sentences
premise_quantities = {}
hypothesis_quantities = {}

# Extract the quantities from the input sentences
for factor in premise_factors:
    premise_quantities[factor] = 1
for factor in hypothesis_factors:
    hypothesis_quantities[factor] = 1

# Compare the quantities in the input sentences
contradiction = False
entailment = False
neutral = False

for factor in premise_quantities:
    if factor in hypothesis_quantities:
        if premise_quantities[factor] > hypothesis_quantities[factor]:
            label = "contradiction"
        elif premise_quantities[factor] < hypothesis_quantities[factor]:
            label = "entailment"
        else:
            label = "neutral"
            break
    else:
        label = "neutral"

print(label)
