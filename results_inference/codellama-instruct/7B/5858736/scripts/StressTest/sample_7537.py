# Define variables for the numerical entities in the premise and hypothesis
premise_scores = [50, 60, 70, 80, 80]
hypothesis_scores = [40, 60, 70, 80, 80]

# Calculate the average score for the premise and hypothesis
premise_average = sum(premise_scores) / len(premise_scores)
hypothesis_average = sum(hypothesis_scores) / len(hypothesis_scores)

# Compare the average scores for the premise and hypothesis
if hypothesis_average >= premise_average:
    # The hypothesis average score is greater than or equal to the premise average score, so the hypothesis is entailed
    label = "entailment"
elif hypothesis_average < premise_average:
    # The hypothesis average score is less than the premise average score, so the hypothesis is not entailed
    label = "contradiction"
else:
    # The hypothesis average score is equal to the premise average score, so the hypothesis is neutral
    label = "neutral"

print(label)
