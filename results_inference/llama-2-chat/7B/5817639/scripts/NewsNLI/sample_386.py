# Define variables for premise and hypothesis
premise_indictment = 1
hypothesis_indictment = 1

# Check if the hypothesis contradicts the premise
if hypothesis_indictment!= premise_indictment:
    # If the hypothesis value is different from the premise value, label it as contradiction
    label = "contradiction"
else:
    # If the hypothesis value is the same as the premise value, label it as entailment
    label = "entailment"

print(label)
