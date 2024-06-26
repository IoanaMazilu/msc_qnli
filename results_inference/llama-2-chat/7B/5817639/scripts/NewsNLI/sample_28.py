# Define variables for premise and hypothesis
premise_box_office = 29300000
hypothesis_box_office = 29300000

# Check if the hypothesis contradicts the premise
if hypothesis_box_office!= premise_box_office:
    label = "contradiction"
else:
    # If the values are the same, we can infer entailment
    label = "entailment"

print(label)
