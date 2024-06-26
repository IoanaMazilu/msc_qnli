# Define variables for premise and hypothesis
premise_cost = 42000000
hypothesis_cost = 42000000

# Check if the hypothesis value matches the premise value
if hypothesis_cost!= premise_cost:
    # If the values differ, check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the values match, check if the hypothesis entails the premise
    label = "entailment"

print(label)
