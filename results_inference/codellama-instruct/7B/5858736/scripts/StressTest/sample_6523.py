premise_scores = [45, 67, 76, 82, 85]
hypothesis_scores = [55, 67, 76, 82, 85]

# the hypothesis talks about the average score obtained by Reeya in different subjects
if sum(hypothesis_scores) / len(hypothesis_scores) <= sum(premise_scores) / len(premise_scores):
    # check if the hypothesis value contradicts the estimate of more than'sum(premise_scores) / len(premise_scores)'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score obtained by Reeya
    # any average score greater than'sum(premise_scores) / len(premise_scores)' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
