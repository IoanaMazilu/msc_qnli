# Define variables for the premise and hypothesis
premise_score = 50
hypothesis_score = 50

# Check if the hypothesis value contradicts the premise value
if hypothesis_score!= premise_score:
    label = "contradiction"
else:
    # If the hypothesis value is the same as the premise value, we can infer entailment
    label = "entailment"

print(label)
