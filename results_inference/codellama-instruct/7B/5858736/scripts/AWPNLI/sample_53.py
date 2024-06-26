# Define variables for the numerical entities in the premise and hypothesis
premise_lambs = 6048.0
premise_white_lambs = 193.0
hypothesis_black_lambs = 5854.0

# Extract all quantities as valid numbers
total_lambs = premise_lambs
total_white_lambs = premise_white_lambs

# Use brief comments to explain what comparison we do between the defined variables
# Check if the number of black lambs in the hypothesis contradicts the number of lambs in the premise
if hypothesis_black_lambs!= total_lambs:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
