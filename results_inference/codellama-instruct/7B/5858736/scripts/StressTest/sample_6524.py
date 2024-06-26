# Define variables for the numerical entities in the premise and hypothesis
premise_scores = [55, 67, 76, 82, 85]
hypothesis_scores = [35, 67, 76, 82, 85]

# Calculate the average for the premise and hypothesis
premise_average = sum(premise_scores) / len(premise_scores)
hypothesis_average = sum(hypothesis_scores) / len(hypothesis_scores)

# Compare the averages
if hypothesis_average >= premise_average:
    # The hypothesis average is greater than or equal to the premise average, so the hypothesis is entailed
    label = "entailment"
elif hypothesis_average < premise_average:
    # The hypothesis average is less than the premise average, so the hypothesis is not entailed
    label = "contradiction"
else:
    # The hypothesis average is equal to the premise average, so the hypothesis is neutral
    label = "neutral"

print(label)
