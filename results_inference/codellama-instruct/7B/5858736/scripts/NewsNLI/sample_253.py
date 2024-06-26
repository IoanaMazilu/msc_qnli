# Define variables for the premise and hypothesis
premise_access_gun = 500
hypothesis_access_gun = 5

# Extract the quantities as valid numbers
premise_access_gun = float(premise_access_gun)
hypothesis_access_gun = float(hypothesis_access_gun)

# Check if the hypothesis values and estimates do not contradict the premise values
if hypothesis_access_gun!= premise_access_gun:
    # Infer entailment
    label = "entailment"
else:
    # Infer neutral
    label = "neutral"

print(label)
