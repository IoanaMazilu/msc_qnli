# Define variables for premise and hypothesis
premise = "366 cartograms"
hypothesis = "366 cartograms include vivid data on disease, wealth, poverty and the environment."

# Extract numbers from premise and hypothesis
premise_numbers = [float(x) for x in premise.split()]
hypothesis_numbers = [float(x) for x in hypothesis.split()]

# Compare variables
if hypothesis_numbers[0]!= premise_numbers[0]:
    # Check if the number of cartograms in the hypothesis contradicts the number of cartograms in the premise
    label = "contradiction"
elif any(hypothesis_numbers[i] - premise_numbers[i] for i in range(1, len(hypothesis_numbers))):
    # Check if any of the numbers in the hypothesis contradict the corresponding numbers in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
