# Define variables for the numerical entities in the premise and hypothesis
premise_birdies = 6
premise_round = 65
hypothesis_birdies = 11
hypothesis_round = 65

# Extract all quantities as valid numbers
premise_birdies = int(premise_birdies)
premise_round = int(premise_round)
hypothesis_birdies = int(hypothesis_birdies)
hypothesis_round = int(hypothesis_round)

# Use brief comments to explain what comparison you do between the defined variables
if premise_birdies!= hypothesis_birdies:
    # Check if the number of birdies in the hypothesis contradicts the number of birdies in the premise
    label = "contradiction"
elif premise_round!= hypothesis_round:
    # Check if the round score in the hypothesis contradicts the round score in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
