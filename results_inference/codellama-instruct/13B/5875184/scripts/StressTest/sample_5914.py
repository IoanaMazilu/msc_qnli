premise_scores = [90, 80, 70, 60]
hypothesis_scores = [90, 80, 70]

# calculate the average score for the premise
premise_average = sum(premise_scores) / len(premise_scores)

# calculate the average score for the hypothesis
hypothesis_average = sum(hypothesis_scores) / len(hypothesis_scores)

# check if the hypothesis average score contradicts the premise average score
if hypothesis_average < premise_average:
    label = "contradiction"
# check if the hypothesis average score is consistent with the premise average score
elif hypothesis_average == premise_average:
    label = "entailment"
# the hypothesis average score is not consistent with the premise average score, but cannot be explicitly entailed from the premise
else:
    label = "neutral"

print(label)
