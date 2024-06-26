average_score_premise = 55 + 67 + 76 + 82 + 85
average_score_hypothesis = 35 + 67 + 76 + 82 + 85

# the hypothesis talks about the scores obtained by Reeya in different subjects, which is also mentioned in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the average scores in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
