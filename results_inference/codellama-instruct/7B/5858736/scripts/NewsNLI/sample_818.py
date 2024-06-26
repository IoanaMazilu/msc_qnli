# Define variables with representative names for the numerical entities in both inputs
percentage_legal_states = 0.72
number_states_allow_marriage = 37

# Extract all quantities as valid numbers (integers or floats)
percentage_legal_states = float(percentage_legal_states)
number_states_allow_marriage = int(number_states_allow_marriage)

# Use brief comments to explain what comparison you do between the defined variables
if percentage_legal_states!= number_states_allow_marriage / 50:
    # Check if the percentage of states where same-sex marriage is legal contradicts the number of states that allow same-sex marriage
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
