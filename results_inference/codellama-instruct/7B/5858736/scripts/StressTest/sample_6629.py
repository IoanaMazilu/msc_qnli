# Define variables for the numerical entities in the premise and hypothesis
premise_scores = [1, 2, 3]
hypothesis_scores = [1, 2, 3]

# Extract all quantities as valid numbers
premise_scores = [int(score) for score in premise_scores]
hypothesis_scores = [int(score) for score in hypothesis_scores]

# Check if the hypothesis values contradict the premise
if any(score > 1 for score in hypothesis_scores):
    label = "contradiction"
elif any(score > 2 for score in hypothesis_scores):
    label = "contradiction"
elif any(score > 3 for score in hypothesis_scores):
    label = "contradiction"
elif any(score < 1 for score in hypothesis_scores):
    label = "contradiction"
elif any(score < 2 for score in hypothesis_scores):
    label = "contradiction"
elif any(score < 3 for score in hypothesis_scores):
    label = "contradiction"
else:
    label = "entailment"

print(label)
