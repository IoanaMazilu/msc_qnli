scores_premise = [55, 67, 76, 82, 85]
scores_hypothesis = [35, 67, 76, 82, 85]
average_premise = sum(scores_premise) / len(scores_premise)
average_hypothesis = sum(scores_hypothesis) / len(scores_hypothesis)

# the hypothesis refers to the scores obtained by Reeya in different subjects mentioned in the premise
if average_hypothesis!= average_premise:
    # check if the average in the hypothesis contradicts the average reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
