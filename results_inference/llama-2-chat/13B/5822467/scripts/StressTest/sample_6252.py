premise_scores = [1, 2, 3, 4]
hypothesis_scores = [less than 7, 2, 3, 4]

# check if the hypothesis scores contradict the premise scores
if any(score not in premise_scores for score in hypothesis_scores):
    label = "contradiction"
elif all(score in premise_scores for score in hypothesis_scores):
    label = "entailment"
else:
    label = "neutral"

print(label)
