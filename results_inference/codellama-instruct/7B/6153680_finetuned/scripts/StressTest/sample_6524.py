scores = [55, 67, 76, 82, 85]

# the hypothesis refers to the same scores as the premise
# compute the average score in the premise
average_score_premise = sum(scores) / len(scores)

# compute the average score in the hypothesis
average_score_hypothesis = sum(scores) / len(scores)

# check if the average score in the hypothesis contradicts the average score in the premise
if average_score_hypothesis!= average_score_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
