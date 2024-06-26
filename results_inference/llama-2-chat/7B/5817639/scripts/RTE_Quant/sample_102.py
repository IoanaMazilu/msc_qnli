# Define variables for the premise and hypothesis
premise_deaths = 4
premise_injured = 80
hypothesis_deaths = 4
hypothesis_injured = 80

# Check if the hypothesis contradicts the premise
if hypothesis_deaths!= premise_deaths or hypothesis_injured!= premise_injured:
    label = "contradiction"
else:
    # If the values in the hypothesis are the same as the values in the premise, we can infer entailment
    label = "entailment"

print(label)
